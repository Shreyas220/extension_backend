from rest_framework import serializers
from .models import timespent

class TimespentSerializer(serializers.ModelSerializer):
    class Meta:
        model = timespent
        fields = '__all__'

    
