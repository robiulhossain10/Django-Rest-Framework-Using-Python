from django.contrib import admin

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'admission_date')
    search_fields = ('name', 'roll_number', 'email')

