from django.urls import path 
from . import views


app_name = "courses"
urlpatterns = [
    path('categories/', views.courses_list, name="CoursesList"),
    path('course/<slug>', views.course_detail, name="CourseDetails"),
]