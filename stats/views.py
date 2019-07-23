from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from stats.serializers import UserSerializer,\
    GroupsSerializer, ChannelsSerializer
from stats.models import User, Group, Channel


class UserViewSet(ModelViewSet):
    lookup_field = 'telegram_id'
    queryset = User.objects.defer("id")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(ModelViewSet):
    lookup_field = 'telegram_id'
    queryset = Group.objects.defer("id")
    serializer_class = GroupsSerializer
    permission_classes = [IsAuthenticated]


class ChannelsViewSet(ModelViewSet):
    lookup_field = 'telegram_id'
    queryset = Channel.objects.defer("id")
    serializer_class = ChannelsSerializer
    permission_classes = [IsAuthenticated]
