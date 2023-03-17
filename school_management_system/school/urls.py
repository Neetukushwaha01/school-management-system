from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('Create', views.SchoolCreateView.as_view()),
    path('StudentBulkCreate', views.StudentBulkCreateView.as_view()),
    path('StudentList', views.StudentListView.as_view()),
    path('StudentUpdate', views.StudentUpdateView.as_view()),
    path('SchoolUpdate', views.SchoolUpdateView.as_view()),
    path('SchoolList', views.SchoolListView.as_view()),


]