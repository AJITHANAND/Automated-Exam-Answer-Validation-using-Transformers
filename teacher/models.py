from django.db import models


# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=2000)
    std = models.CharField(max_length=200)

    def __str__(self):
        return self.question
