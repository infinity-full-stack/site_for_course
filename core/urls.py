from django.urls import path
from .views import home, course_students, student_detail,create_course,update_course,create_student,update_student,delete_course,delete_student

urlpatterns = [
    path('', home, name='home'),
    path('course/<int:course_id>/students/', course_students, name='course_students'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),

    path('add/course/', create_course, name='create_student'),
    path('add/student/',create_student,name='create_student'),
    path('course/update/<int:course_id>/',update_course,name='update_course'),
    path('student/update/<int:student_id>/',update_student,name='update_student'),
    path('course/delete/<int:course_id>/',delete_course,name='delete_course'),
    path('student/delete/<int:student_id>/',delete_student,name='delete_student')

]
