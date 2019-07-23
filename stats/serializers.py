from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from stats.models import User, Groups, Channels, UserStatus


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class ChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = '__all__'


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=UserStatus.objects.all(),
            fields=['user', 'channel', 'group'])
            ]
