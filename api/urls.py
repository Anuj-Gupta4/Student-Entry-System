# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name="ApiOverview"),
    path('StudentList', views.StudentList.as_view(), name="StudentList"),
    path('StudentDetail/<id>/', views.StudentDetail.as_view(), name="StudentDetail"),
]
