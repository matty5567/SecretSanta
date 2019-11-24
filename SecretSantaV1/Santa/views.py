from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
import random


from random import randint


def Randomiser(request):
    users = User.objects.all()
    list1 = ['name']
    for i in range(0, len(users)):
        b = randint(0, len(users)-1)
        while (users[b].username in list1) or (b == i):
            b = randint(0, len(users)-1)

        users[b].profile.SecretSanta = users[i].username
        users[b].profile.SecretSantaEmail = users[i].email
        users[i].profile.Assigned = users[b].username
        users[i].profile.AssignedEmail = users[b].email
        users[i].profile.SSWW1 = users[b].profile.WishListItem1
        users[i].profile.SSWW2 = users[b].profile.WishListItem2
        users[i].profile.SSWW3 = users[b].profile.WishListItem3
        users[b].profile.save()
        users[i].profile.save()

        list1.append(users[b].username)

        messages.success(request, User.objects.all()[i].username + " has been assigned " + users[b].username)



    return redirect('/admin')




