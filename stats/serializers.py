from rest_framework import serializers
from stats.models import User, UserStatus, GroupsAndChannels


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "all"