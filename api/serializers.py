from rest_framework import serializers
from .models import Application, ENTITY_TYPE
from rest_framework import exceptions


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'fio', 'phone_num', 'donate_amount', 'entity_type', 'firm_name']

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
