"""serializers"""
from rest_framework import serializers

from common.gda.serializers import DynamicFieldsModelSerializer
from common.party.models import *


class PartySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer
