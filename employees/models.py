from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
# Create your models here.

class Member(models.Model):
  username = models.CharField(max_length=225, default= "")
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  position=models.CharField(max_length=200)
  password = models.CharField(max_length=255, default = "")
  email = models.EmailField(default = "")
  salary=models.IntegerField()
  work_hours=models.IntegerField()
  # user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  # test=models.BooleanField(default=True)

  def __str__(string):
    return string.firstname
  
class  Managers(models.Model):
  username = models.CharField(max_length = 255)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  email = models.EmailField()

class Task(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  due_date = models.DateField()
  status = models.CharField(max_length=20, choices=(
      ('assigned', 'Assigned'),
      ('in_progress', 'In Progress'),
      ('completed', 'Completed'),
    ))
  assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE)

  assigned_by = models.ForeignKey(Managers , on_delete=models.CASCADE, default = "", null = True)
