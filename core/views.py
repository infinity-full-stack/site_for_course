from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import CourseForm,StudentForm

def home(request):
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

# --------------------------- start Course ------------------------------------------
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()

    context = {
        'form': form
    }

    return render(request,'core/add_course.html',context)

# --------------------------- end Course --------------------------------------------


# --------------------------- update Course ---------------------------------------------
def update_course(request,course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseForm(data=request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CourseForm(instance=course)

    context = {
        'form': form
    }

    return render(request,'core/update_course.html',context)
# --------------------------- end update Course ------------------------------------------


# --------------------------- create  Student --------------------------------------------
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    context = {
        'form': form
    }

    return render(request,'core/add_student.html',context)
# --------------------------- end  Student -----------------------------------------------

# --------------------------- update Student ---------------------------------------------
def update_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form
    }

    return render(request,'core/update_student.html',context)
# --------------------------- end update Student -----------------------------------------

# --------------------------- delete Course   --------------------------------------------
def delete_course(request,course_id):
    course = Course.objects.get(pk=course_id)

    if request.method == 'POST':
        course.delete()
        return redirect('home')

    context = {
        'course': course
    }

    return render(request,'core/delete_course.html',context)
# --------------------------- end delete Course ------------------------------------------

# --------------------------- delete Student  --------------------------------------------
def delete_student(request,student_id):
    student = Student.objects.get(pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    context = {
        'student': student
    }

    return render(request,'core/delete_student.html',context)
# --------------------------- end delete Student  ----------------------------------------