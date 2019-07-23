from django.contrib import admin
from .models import User, Groups, Channels, UserStatus

admin.register(User)
admin.register(Groups)
admin.register(Channels)
admin.register(UserStatus)
