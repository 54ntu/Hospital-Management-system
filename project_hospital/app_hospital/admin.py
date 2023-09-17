from django.contrib import admin
from .models import patientModel

# Register your models here.
class  patientAdminModel(admin.ModelAdmin):
    list_display= ('firstname','lastname','age','sex')



admin.site.register(patientModel,patientAdminModel)
