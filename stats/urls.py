from stats.views import UserView

# from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('user/', UserView.as_view, name='user-list')
]
