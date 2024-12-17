from django.urls import path
from . import views
urlpatterns = [
    path("",views.all_courses,name="home"),
    path("register/",views.register,name="register"),
    path("students Details/", views.students,name="students"),
    path("course_students/<int:id>/",views.course_std,name="course_std")
    ]