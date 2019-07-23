from rest_framework import serializers

from stats.models import User, Group, Channel


class TelegramIDSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.telegram_id


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id']


class ChannelsSerializer(serializers.ModelSerializer):
    users = TelegramIDSerializer(many=True, read_only=True)
    linked_group = TelegramIDSerializer(read_only=True)

    class Meta:
        model = Channel
        exclude = ['id']


class GroupsSerializer(serializers.ModelSerializer):
    users = TelegramIDSerializer(many=True, read_only=True)
    linked_channel = TelegramIDSerializer(read_only=True)

    class Meta:
        model = Group
        exclude = ['id']
