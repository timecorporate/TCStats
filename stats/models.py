from django.db import models
# Create your models here.


class User(models.Model):
    telegram_id = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=32, blank=False, unique=True)

    def __str__(self):
        return self.first_name


class GroupsAndChannels(models.Model):
    telegram_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    is_group = models.BooleanField(default=True)
    users = models.ManyToManyField(User, through='UserStatus')

    def __str__(self):
        return self.title


class UserStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupsAndChannels, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    user_state = models.CharField(max_length=10)
