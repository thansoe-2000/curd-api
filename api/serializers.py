from rest_framework import serializers
from .models import *

class LessonSerializer(serializers.ModelSerializer):
     class Meta:
          model = Lesson
          fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Student
          fields = "__all__"