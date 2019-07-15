from django.contrib import admin
from .models import User, Groups, Channels, UserStatus
# Register your models here.

admin.register(User)
admin.register(Groups)
admin.register(Channels)
admin.register(UserStatus)
