from rest_framework import serializers
from .models import GeeksModel


class GeeksSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeeksModel
        fields = '__all__'