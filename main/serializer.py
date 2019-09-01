from rest_framework import serializers
from .models import *

class LabsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Labs
        fields = '__all__'