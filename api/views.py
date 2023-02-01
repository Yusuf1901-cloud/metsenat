from . import models
from rest_framework import generics, views
from . import serializers
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


class ApplicationCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer


class ApplicationListView(generics.ListAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'donate_amount', 'created']


class ApplicationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer


class UniversityListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


class StudentCreateAPIView(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'otm']


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentBenefactorsListAPIView(generics.ListAPIView):
    queryset = models.SponsorShip.objects.all()
    serializer_class = serializers.StudentsSponsorListSerializer

    def get_queryset(self):
        stu_id = self.kwargs.get('pk')
        qs = models.SponsorShip.objects.filter(student_id=stu_id)
        return qs


class StudentBenefactorsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SponsorShip.objects.all()
    serializer_class = serializers.StudentsSponsorListSerializer

    def get_queryset(self):
        stu_id = self.kwargs.get('pk')
        stu_benefactor_id = self.kwargs.get('lk')
        qs = models.SponsorShip.objects.filter(student_id=stu_id, application_id=stu_benefactor_id).first()
        return qs


class SponsorShipListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.SponsorShip.objects.all()
    serializer_class = serializers.SponsorShipSerializer


class DashboardAPIView(generics.ListAPIView):
    queryset = models.Dashboard.objects.all()
    serializer_class = serializers.DashboardSerializer

    # def get_queryset(self):
    #     year = self.request.query_params.get('year', 2022)
    #     qs = models.Student.objects.all().annotate()
