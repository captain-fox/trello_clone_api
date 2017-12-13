from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

import uuid


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Board(models.Model):
    boardTitle = models.TextField(max_length=50, blank=False, unique=True)
    boardDescription = models.TextField(max_length=500, blank=True)
    private_access = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE)


class Table(models.Model):
    tableTitle = models.TextField(max_length=50, blank=False, unique=True)
    tableDescription = models.TextField(max_length=500, blank=True)
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='tables', on_delete=models.CASCADE)


class Card(models.Model):
    archiveStatus = models.BooleanField(default=False)
    title = models.TextField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    uniqueNumber = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    owner = models.ForeignKey('auth.User', related_name='cards', on_delete=models.CASCADE)
    tableID = models.ForeignKey(Table, on_delete=models.CASCADE)




