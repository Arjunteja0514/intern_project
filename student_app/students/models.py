from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    school = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')

class Task(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateField()
    is_completed = models.BooleanField(default=False)


# Create your models here.
