from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    sem=models.CharField(max_length=1)
