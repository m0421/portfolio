from django.contrib import admin

from .models import Profile, Description, Skills, Work
# Register your models here.

admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Skills)
admin.site.register(Work)