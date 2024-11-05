from django import forms
from .models import Profile, Task

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'school', 'age', 'city', 'profile_pic']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'date_due', 'is_completed']
