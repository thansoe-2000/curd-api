from django.urls import path
from . import views

urlpatterns = [
     path('', views.apiOverview, name='apiOverview'),

     # lesson comments
     path('lesson-lists/', views.lessonList, name='lesson-lists'),
     path('lesson-detail/<str:pk>/', views.lessonDetail, name='lesson-detail'),
     path('lesson-create/', views.lessonCreate, name='lesson-create'),
     path('lesson-update/<str:pk>/', views.lessonUpdate, name='lesson-update'),
     path('lesson-delete/<str:pk>/', views.lessonDelete, name='lesson-delete'),


     # students comments
     path('student-lists/', views.studentList, name='student-lists'),
     path('student-detail/<str:pk>', views.studentDetail, name='student-detail'),
     path('student-delete/<str:pk>', views.studentDelete, name='student-delete'),
     path('student-update/<str:pk>', views.studentUpdate, name='student-update'),
     path('student-create/', views.studentCreate, name='student-create'),


]