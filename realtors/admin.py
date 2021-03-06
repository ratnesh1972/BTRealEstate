from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp')
    list_editable = ('is_mvp',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Realtor, RealtorAdmin)
