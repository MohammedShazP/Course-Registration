from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Students
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
# below is the function to load the page where all courses are listed out.
def all_courses(request):
    # Details of courses are fetched from course table
    courses = Course.objects.all()
    context = {"courses": courses, }

    return render(request, "registration/courses.html", context)


# below is the function to register the students for course.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            entered_data = form.save()
            # below is the code for checking whether maximum capacity of the requested course exceed.
            courses = entered_data.enrolled_course.all()
            for course in courses:
                if course.maximum_capacity > course.current_enrolled:
                    course.current_enrolled += 1
                    course.save()
                else:
                    # if the course is full an error message will be given and the data will be deleted.
                    form.add_error("enrolled_course", f"Sorry, {course.title} is full.")
                    context = {"form": form}
                    entered_data.delete()
                    return render(request, "registration/register.html", context)
            messages.success(request,"Your registration is successfully completed.")
            return redirect("register")

    form = RegisterForm()
    context = {"form": form}
    return render(request, "registration/register.html", context)

def students(request):
    students = Students.objects.all()
    context = {'students' : students}
    return render(request,"registration/students.html",context)

def course_std(request, id):
    # print("this is the id", id)
    std_name = Course.objects.get(pk=id)
    context = {"std_name" : std_name}
    return render(request,"registration/course_students.html",context)

def de_register(request,id):
    std_data = Students.objects.get(id=id)
    if std_data:
        std_data.delete()
    else:
        raise f"invalid operations"



