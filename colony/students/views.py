from django.shortcuts import render
from .models import*

# Create your views here.
from django.http import HttpResponse # this response will be shown in our browser

def home(request):
    # return render("Welcome, this is the Student's home page")
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except:
        student = None
    return render(request, 'student.html', {'student': student})



