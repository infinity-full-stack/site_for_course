from django.urls import path
from .views import index, course_students, student_detail

urlpatterns = [
    path('', index, name='index'),
    path('course/<int:course_id>/students/', course_students, name='course_students'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
]
