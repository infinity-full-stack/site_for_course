from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Course, Student
from .forms import CourseForm, StudentForm


def home(request):
    courses = Course.objects.all()
    q = request.GET.get('q', '')
    if q:
        students = Student.objects.filter(full_name__icontains=q)
    else:
        students = Student.objects.all()
    p = Paginator(students, 3)
    page = p.page(request.GET.get('page', 1))
    return render(request, 'core/index.html', {'courses': courses, 'page': page, 'q': q})


def course_students(request, course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course_id=course_id)
    return render(request, 'core/course_students.html', {'courses': courses, 'students': students})


def student_detail(request, student_id):
    courses = Course.objects.all()
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/student_detail.html', {'courses': courses, 'student': student})


@login_required(login_url='login_view')
@permission_required('core.add_course')
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'core/add_course.html', {'form': form})


@login_required(login_url='login_view')
@permission_required('core.change_course')
def update_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm(instance=course)
    return render(request, 'core/update_course.html', {'form': form})


@login_required(login_url='login_view')
@permission_required('core.add_student')
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'core/add_student.html', {'form': form})


@login_required(login_url='login_view')
@permission_required('core.change_student')
def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/update_student.html', {'form': form})


@login_required(login_url='login_view')
@permission_required('core.delete_course')
def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('home')
    return render(request, 'core/delete_course.html', {'course': course})


@login_required(login_url='login_view')
@permission_required('core.delete_student')
def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'core/delete_student.html', {'student': student})