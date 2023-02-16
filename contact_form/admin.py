from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    pass
