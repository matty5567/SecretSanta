from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    WishListItem1 = models.TextField(max_length=40, blank=True)
    WishListItem2 = models.CharField(max_length=40, blank=True)
    WishListItem3 = models.CharField(max_length=40, blank=True)
    SecretSanta = models.CharField(max_length=40, blank=True)
    Assigned = models.CharField(max_length=40, blank=True)
    SSWW1 = models.CharField(max_length=40, blank=True)
    SSWW2 = models.CharField(max_length=40, blank=True)
    SSWW3 = models.CharField(max_length=40, blank=True)
    SecretSantaEmail = models.CharField(max_length=40, blank=True)
    AssignedEmail = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username

