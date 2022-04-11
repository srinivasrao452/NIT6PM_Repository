
from django  import  forms
from studentapp.models import Student

class Student_ModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
