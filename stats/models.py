from django.db import models


class User(models.Model):
    telegram_id = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=32, blank=False, unique=True)

    def __str__(self):
        return self.first_name


class Channel(models.Model):
    telegram_id = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Group(models.Model):
    telegram_id = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    linked_channel = models.OneToOneField(Channel,
                                          null=True,
                                          on_delete=models.CASCADE,
                                          related_name="linked_group")

    def __str__(self):
        return self.title
