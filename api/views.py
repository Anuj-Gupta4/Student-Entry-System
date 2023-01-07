from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List': '/StudentList',                # Use GET
        'Create': '/StudentList',              # Use POST
        'Detail': '/StudentDetail/<id>/',      # Use GET
        'Update': '/StudentDetail/<id>/',      # Use PUT
        'Delete': '/StudentDetail/<id>/',      # Use DELETE
        }
    return Response(api_urls)


class StudentList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # restrict access to admins only
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)    


class StudentDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    # restrict access to admins only
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

