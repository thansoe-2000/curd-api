from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
     api_urls = {
          # lesson
          'Lesson List':'/lesson-lists/',
          'Lesson Detail':'/lesson-detail/<str:pk>/',
          'Lesson Update':'/lesson-update/<str:pk>/',
          'Lesson Delete':'/lesson-delete/<str:pk>/',
          'Lesson Create':'/lesson-create/',

          # students
          'Student List':'/student-lists/',
          'Student Detail':'/student-detail/<str:pk>/',
          'Student Update':'/student-update/<str:pk>/',
          'Student Delete':'/student-delete/<str:pk>/',
          'Student Create':'/student-create/',

     }
     return Response(api_urls)
         

# get method
@api_view(['GET'])
def lessonList(request):
     lessons = Lesson.objects.all()
     serializer = LessonSerializer(lessons, many=True)
     return Response(serializer.data)

# get method
@api_view(['GET'])
def lessonDetail(request, pk):
     lesson = Lesson.objects.get(id=pk)
     serializer = LessonSerializer(lesson, many=False)
     return Response(serializer.data)

# post method
@api_view(['POST'])
def lessonCreate(request):
     serializer = LessonSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

# post method
@api_view(['POST'])
def lessonUpdate(request, pk):
     lesson = Lesson.objects.get(id=pk)
     serializer = LessonSerializer(instance=lesson, data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

# delete method
@api_view(['DELETE'])
def lessonDelete(request, pk):
     lesson = Lesson.objects.get(id=pk)
     lesson.delete
     return Response("Lesson successfully delete!")

# use get method
@api_view(['GET'])
def studentList(request):
     students = Student.objects.all()
     serializer = StudentSerializer(students, many=True)
     return Response(serializer.data)


# user get method
@api_view(['GET'])
def studentDetail(request, pk):
     student = Student.objects.get(id=pk)
     serializer = StudentSerializer(student, many=False)
     return Response(serializer.data)

# use post method for update
@api_view(['POST'])
def studentUpdate(request, pk):
     student = Student.objects.get(id=pk)
     serializer = StudentSerializer(instance=student, data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)


# use post method for create
@api_view(['POST'])
def studentCreate(request, pk):
     serializer = StudentSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(rerializer.data)

# use delete method for delete
@api_view(['DELETE'])
def studentDelete(request, pk):
     student = Student.objects.get(id=pk)
     student.delete()
     return Response("Student successfully delete")
