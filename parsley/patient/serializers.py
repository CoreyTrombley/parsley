from django.contrib.auth.models import User, Group
from rest_framework import serializers

from parsley.patient.models import Patient
from parsley.address.serializers import AddressSerializer
from parsley.phone.serializers import PhoneSerializer
from parsley.address.models import Address
from parsley.phone.models import Phone

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    phones = PhoneSerializer(many=True)

    class Meta:
        model = Patient
        fields = [ 'url', 'first_name', 'middle_name', 'last_name',
                  'phones', 'email', 'dob', 'age', 'gender', 'status',
                  'terms_accepted', 'terms_accepted_at', 'address',]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        phones_data = validated_data.pop('phones')

        patient = Patient.objects.create(**validated_data)

        Address.objects.create(patient=patient, **address_data)
        for phone_data in phones_data:
            Phone.objects.create(patient=patient, **phone_data)

        return patient

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
