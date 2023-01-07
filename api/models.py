from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Address = models.CharField(max_length=300)
    Grade = models.CharField(max_length=100)
    Major = models.CharField(max_length=200)

    def __str__(self):
        return self.Name