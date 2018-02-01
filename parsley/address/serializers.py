from rest_framework import serializers

from parsley.address.models import Address

class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = ['line_1', 'line_2', 'city', 'state', 'zip']
