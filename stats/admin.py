from django.contrib import admin
from .models import User, GroupsAndChannels, UserStatus
# Register your models here.

admin.register(User)
admin.register(GroupsAndChannels)
admin.register(UserStatus)