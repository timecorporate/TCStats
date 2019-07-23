from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from stats.serializers import UserSerializer,\
    GroupsSerializer, ChannelsSerializer, UserStatusSerializer
from stats.models import User, Groups, Channels, UserStatus


class UserViewSet(ModelViewSet):
    lookup_field = 'telegram_id'
    queryset = User.objects.defer("id")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(ModelViewSet):
    lookup_field = 'telegram_id'
    queryset = Groups.objects.defer("id")
    serializer_class = GroupsSerializer
    permission_classes = [IsAuthenticated]


class ChannelsViewSet(ModelViewSet):
    lookup_field = 'telegram_id'
    queryset = Channels.objects.defer("id")
    serializer_class = ChannelsSerializer
    permission_classes = [IsAuthenticated]


class UserStatusViewSet(ModelViewSet):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer
    permission_classes = [IsAuthenticated]
