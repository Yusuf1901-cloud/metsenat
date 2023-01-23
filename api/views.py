from django.shortcuts import render
from .models import Application
from rest_framework.generics import ListCreateAPIView
from .serializers import ApplicationSerializer
from rest_framework.parsers import JSONParser
from rest_framework import permissions


class ApplicationListCreateView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
