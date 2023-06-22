from django.contrib import admin
from .models import PersonalNote

# Register your models here.
admin.site.register(PersonalNote)
admin.site.site_title = "Notes Admin"
admin.site.site_header = "Notes Admin"
admin.site.index_title = "Welcome to Notes Admin"
