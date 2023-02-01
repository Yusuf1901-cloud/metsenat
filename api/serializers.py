from rest_framework import serializers
from . import models
from rest_framework import exceptions
from django.db.models import Sum


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ['id', 'fio', 'phone_num', 'donate_amount', 'entity_type', 'firm_name', 'status']

    def create(self, validated_data):
        print(validated_data)

        phone_number = validated_data.get('phone_num')
        if not (9 <= len(phone_number) <= 13):
            raise exceptions.ValidationError(f"You have entered incorrect phone number: {phone_number}")

        firm = validated_data.get('firm_name')
        entity_type = validated_data.get('entity_type')
        if entity_type == 'PHY' and len(firm) > 0:
            raise exceptions.ValidationError(f'Physical benefactors usually don\'t have organisation '
                                             f'which you have entered {firm} !!!')

        return super().create(validated_data)


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.University
        fields = ['id', 'title']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'fio', 'otm', 'type', 'cont_amount', 'phone_num']

    def create(self, validated_data):
        phone_number = validated_data.get('phone_num')
        if not 9 <= len(phone_number) <= 13:
            raise exceptions.ValidationError(f"you have entered invalid phone number==> {phone_number}")

        return super().create(validated_data)


class StudentListSerializer(serializers.ModelSerializer):
    all_dist_amount = serializers.SerializerMethodField()

    class Meta:
        model = models.Student
        fields = ['id', 'fio', 'otm', 'type', 'cont_amount', 'phone_num', 'all_dist_amount']

    def get_all_dist_amount(self, obj):
        return models.SponsorShip.objects.filter(student=obj).aggregate(Sum('dist_amount')).get('dist_amount__sum', 0)


class ApplicationListSerializer(serializers.ModelSerializer):
    sponsor_all_dist_amount = serializers.SerializerMethodField()

    class Meta:
        model = models.Application
        fields = ['id', 'fio', 'phone_num', 'donate_amount', 'entity_type', 'firm_name', 'status', 'sponsor_all_dist_amount']

    def get_sponsor_all_dist_amount(self, obj):
        return models.SponsorShip.objects.filter(application=obj).aggregate(Sum('dist_amount')).get('dist_amount__sum', 0)


class SponsorShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SponsorShip
        fields = ['id', 'student', 'application', 'dist_amount']

    def create(self, validated_data):
        dist_amount = validated_data.get('dist_amount')
        stu = validated_data.get('student')
        app = validated_data.get('application')
        stu_cont_amount = validated_data.get('student').cont_amount
        app_amount = validated_data.get('application').donate_amount

        student_all_dist_amount = models.SponsorShip.objects.filter(student=stu).aggregate(Sum('dist_amount'))\
                                                                                .get('dist_amount__sum', 0)
        sponsor_all_donate_amount = models.SponsorShip.objects.filter(application=app).aggregate(Sum('dist_amount'))\
                                                                                 .get('dist_amount__sum')

        print(student_all_dist_amount)
        if dist_amount + sponsor_all_donate_amount <= app_amount:
            if stu_cont_amount >= student_all_dist_amount + dist_amount:
                return super().create(validated_data)
            else:
                raise exceptions.ValidationError(f"This student's cont_amount is less than all ==> "
                                                 f"{student_all_dist_amount} distributed_amount and "
                                                 f"you have donated {dist_amount} this time")
        else:
            raise exceptions.ValidationError(f"You cannot donate {dist_amount} because ==> "
                                             f"This benefactor has {app_amount},  "
                                             f"thus you are donating {dist_amount}!!")


class SponsorsFIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ['fio']


class StudentsSponsorListSerializer(serializers.ModelSerializer):
    benefactors_fio = serializers.SerializerMethodField()

    class Meta:
        model = models.SponsorShip
        fields = ['id', 'student', 'benefactors_fio', 'dist_amount']

    def get_benefactors_fio(self, obj):
        sponsors = models.Application.objects.filter(sponsorship=obj)
        return SponsorsFIOSerializer(sponsors, many=True).data


class DashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dashboard
        fields = ['asked_amount', 'required_amount', 'paid_amount']
