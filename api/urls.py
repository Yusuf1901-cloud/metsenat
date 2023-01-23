from django.urls import path
from . import views

urlpatterns = [
    path('apps/', views.ApplicationListCreateView.as_view(), name='app-list-create'),
]
