from stats.views import UserCreateListView,\
    GroupsCreateListView, ChannelsCreateListView

# from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('user/', UserCreateListView.as_view(), name='user-list'),
    path('group/', GroupsCreateListView.as_view(), name='groups-list'),
    path('channel/', ChannelsCreateListView.as_view(), name='channels-list'),
]
