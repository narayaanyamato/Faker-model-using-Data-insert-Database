from django.db import models

class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=28)
    sroll=models.IntegerField()
    email=models.EmailField()
    dob=models.DateField()
    mark=models.IntegerField()
    phone=models.BigIntegerField()
    address=models.TextField()

