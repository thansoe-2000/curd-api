from django.db import models

# Create your models here.


class Lesson(models.Model):
     name = models.CharField(max_length=200)
     complete = models.BooleanField(default=False, blank=True, null=True)

     def __str__(self):
          return self.name

class Student(models.Model):
     name = models.CharField(max_length=200)
     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
     complete = models.BooleanField(default=False, blank=True, null=True)

     def __str__(self):
          return self.name
