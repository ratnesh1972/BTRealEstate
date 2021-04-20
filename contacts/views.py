from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            userid = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=userid)
            if has_contacted:
                messages.error(
                    request, 'You already made enquiry for this property!')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, user_id=user_id,
                          name=name, email=email, phone=phone, message=message)
        contact.save()
        # send_mail(
        #     'Property Enquiry',
        #     'Thanks for the enquiry. We will get back to you soon. We appriciate your patience',
        #     'ratnesh.designs@gmail.com',
        #     ['ratneshpatil117@gmail.com'],
        #     fail_silently=False,
        # )
        messages.success(request, 'Enquiry send successfully!')
        return redirect('/listings/'+listing_id)
    else:
        messages.error(request, 'Error in submission!')
        return redirect('/listings/'+listing_id)
