from rest_framework import serializers
from stats.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "all"
