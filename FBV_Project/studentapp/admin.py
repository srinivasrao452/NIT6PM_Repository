
from django.contrib import admin
from studentapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','marks','email','address']

admin.site.register(Student, StudentAdmin)
