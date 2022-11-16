
from rest_framework import serializers
from .models import Nivel

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = ('id', 'name', 'release_date', 'dni', 'category','category_perfil')