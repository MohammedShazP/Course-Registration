from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Students
from .forms import RegisterForm


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
            return redirect("")

    form = RegisterForm()
    context = {"form": form}
    return render(request, "registration/register.html", context)
