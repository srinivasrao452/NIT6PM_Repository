
from django.contrib import admin
from studentapp.models import Student

# Create Student Admin Class
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','marks','email','address']

# register our model name with admin site
admin.site.register(Student, StudentAdmin)
