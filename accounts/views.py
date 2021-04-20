from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # 1. check passwords match.
        if password == password2:
            # 2. check username.
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken!')
                return redirect('register')
            else:
                # 3. check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is taken!')
                    return redirect('register')
                else:
                    # 4. Looks good.
                    user = User.objects.create(
                        password=password, username=username, first_name=first_name, last_name=last_name, email=email)
                    # login after registration.
                    # auth.login(request, user)
                    # messages.success(request, 'User registered successfully!')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'User registered successfully!')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'logged out!')
        return redirect('index')


def dashboard(request):
    contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)
