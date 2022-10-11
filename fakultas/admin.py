from django.contrib import admin
from . models import DosenFkip, StaffFkip, MahasiswaFkip

# Register your models here.

admin.site.register(DosenFkip)
admin.site.register(StaffFkip)
admin.site.register(MahasiswaFkip)