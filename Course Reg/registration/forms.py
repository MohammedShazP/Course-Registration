from django import forms
from .models import Students, Course


# registration form accrding to the course model is created below.
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
