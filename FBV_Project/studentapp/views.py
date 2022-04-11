
from django.shortcuts import render, redirect
from studentapp.models import Student
from studentapp.forms import Student_ModelForm

import  datetime

def StudentListView(request):
    present_time = datetime.datetime.now()
    student_list = Student.objects.all() #  [ ]  |  [{},{},{},...]
    context = {
        "student_list" : student_list,
        "present_time" : present_time
    }
    return render(request, 'studentapp/student_list.html', context)


def StudentCreateView(request):
    if request.method=='POST':
        form = Student_ModelForm(request.POST)

        if form.is_valid():
            form.save() #  store into database
            return redirect('student_list')

    else:
        form = Student_ModelForm()
        context = {
            "form" : form
        }
        return render(request, 'studentapp/student_create.html', context)


def StudentUpdateView(request, pk):
    global student
    if request.method=="POST":
        form = Student_ModelForm(request.POST, instance=student)

        if form.is_valid():
            form.save() # reading data and storing into database
            return redirect('student_list')  #  using aliace name

            # return redirect('/students/{{<int:pk>}}/update/')  #  using  url name
            # return redirect(StudentListView) # StudentListView
        else:
            context ={
                "error" : "Student Object not updated successfully!"
            }
            return render(request, 'studentapp/student_update.html', context)

    else:
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            context ={
                "error" : "Requested Student object not available"
            }
            # return render(request, 'studentapp/student_update.html', context)
        else:
            context = {
                "student" : student
            }
        return render(request, 'studentapp/student_update.html', context)


def StudentDeleteView(request,pk):
    global student
    if request.method=="POST":
        student.delete()
        return redirect('student_list')
    else:
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            context ={
                "error" : "Requested Student object not available"
            }
            return render(request, 'studentapp/student_delete.html', context)
        else:
            context = {
                "student" : student
            }
            return render(request, 'studentapp/student_delete.html', context)


def StudentDetailView(request,pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        context = {
            "error": "Requested Student object not available"
        }
        return render(request, 'studentapp/student_detail.html', context)
    else:
        context = {
            "student": student
        }
        return render(request, 'studentapp/student_detail.html', context)


import datetime
def Date_Time_View(request):
    present_time = datetime.datetime.now()
    context = {
        "present_time" : present_time
    }
    return render(request, 'studentapp/display_time.html', context)
















