from rest_framework import serializers

from blog.models import Lugat

class LugatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugat
        fields = ('id', 'name', 'description')