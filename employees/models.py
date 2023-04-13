from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  position=models.CharField(max_length=200)
  salary=models.IntegerField()
  work_hours=models.IntegerField()
  user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  test=models.BooleanField(default=True)

  def __str__(string):
    return string.firstname

class Task(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  due_date = models.DateField()
  status = models.CharField(max_length=20, choices=(
      ('assigned', 'Assigned'),
      ('in_progress', 'In Progress'),
      ('completed', 'Completed'),
    ))
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

  '''class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
  '''
