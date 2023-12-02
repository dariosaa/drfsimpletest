from rest_framework import serializers
from .models import Proyect

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id','title','descripcion','technology','created_at')
        read_only_fields = ('created_at',)