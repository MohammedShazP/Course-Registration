from django.db import models

# Create your models here.
# Course model is created
class Course(models.Model):
    title = models.CharField(max_length= 150)
    description = models.CharField(max_length= 300)
    maximum_capacity = models.IntegerField()
    current_enrolled = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# student model is created
class Students(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length=250)
    enrolled_course = models.ManyToManyField(Course, related_name="enrolled_course")

    def __str__(self):
        return self.name

