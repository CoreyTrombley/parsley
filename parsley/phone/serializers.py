from rest_framework import serializers

from parsley.phone.models import Phone

class PhoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Phone
        fields = ['type', 'number']

