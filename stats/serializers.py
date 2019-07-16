from rest_framework import serializers
from stats.models import User, Groups, Channels


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id']


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        exclude = ['id']


class ChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        exclude = ['id']
