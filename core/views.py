from django.shortcuts import render, get_object_or_404
from .models import Course, Student


def index(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    return render(request, 'core/index.html', {'courses': courses, 'students': students})


def course_students(request, course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course_id=course_id)
    return render(request, 'core/course_students.html', {'courses': courses, 'students': students})


def student_detail(request, student_id):
    courses = Course.objects.all()
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/student_detail.html', {'courses': courses, 'student': student})
