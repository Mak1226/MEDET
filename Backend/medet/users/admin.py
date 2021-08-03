from django.contrib import admin
from .models import Profile,Medicine,Doctor,Disease

# Register your models here.
admin.site.register(Profile)
admin.site.register(Medicine)
admin.site.register(Disease)
admin.site.register(Doctor)