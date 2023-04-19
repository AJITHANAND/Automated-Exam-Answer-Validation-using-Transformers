from django.db import models


class Student(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=100)
    std_class = models.CharField(max_length=100)
    register_num = models.CharField(max_length=100)


class Login(models.Model):
    email = models.EmailField(max_length=254,)
    password = models.CharField(max_length=255)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

