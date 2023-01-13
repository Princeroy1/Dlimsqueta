from django.contrib import admin
from .models import Client

@admin.register(Client)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','cnic','Driver_name']