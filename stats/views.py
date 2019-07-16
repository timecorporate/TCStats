from rest_framework import generics
from stats.serializers import UserSerializer,\
    GroupsSerializer, ChannelsSerializer
from stats.models import User, Groups, Channels


class UserCreateListView(generics.ListCreateAPIView):
    queryset = User.objects.defer("id")
    serializer_class = UserSerializer


class GroupsCreateListView(generics.ListCreateAPIView):
    queryset = Groups.objects.defer("id")
    serializer_class = GroupsSerializer


class ChannelsCreateListView(generics.ListCreateAPIView):
    queryset = Channels.objects.defer("id")
    serializer_class = ChannelsSerializer
