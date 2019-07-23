from django.db import models


class User(models.Model):
    telegram_id = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=32, blank=False, unique=True)

    def __str__(self):
        return self.first_name


class Channels(models.Model):
    telegram_id = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='UserStatus')

    def __str__(self):
        return self.title


class Groups(models.Model):
    telegram_id = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='UserStatus')
    linked_channel = models.OneToOneField(Channels,
                                          null=True,
                                          on_delete=models.CASCADE)


class UserStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField()
    user_state = models.CharField(max_length=10)
