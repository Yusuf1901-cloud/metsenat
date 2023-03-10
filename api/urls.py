from django.urls import path
from . import views

urlpatterns = [
    path('apps/create/', views.ApplicationCreateView.as_view(), name='app-create'),
    path('apps/list/', views.ApplicationListView.as_view(), name='app-list'),
    path('apps/<int:pk>/', views.ApplicationDetailAPIView.as_view(), name='app-detail'),
    path('universities/', views.UniversityListCreateAPIView.as_view(), name='uni-list-create'),
    path('students/create/', views.StudentCreateAPIView.as_view(), name='student-create'),
    path('students/list/', views.StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailAPIView.as_view(), name='student-detail'),
    path('students/<int:pk>/donates/', views.StudentBenefactorsListAPIView.as_view(),
         name='student-benefactors-list'),
    path('students/<int:stu_id>/donates/<int:pk>/', views.StudentDonatesDetailAPIView.as_view(),
         name='student-benefactors-detail'),
    path('donate/', views.SponsorShipListCreateAPIView.as_view(), name='donate-list-create'),
    path('dashboard/', views.DashboardAPIView.as_view(), name='dashboard'),
]
