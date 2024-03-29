from django.core.mail import send_mail
from .forms import ProfileForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.template.loader import render_to_string
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse



def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid:
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('home')


def ContactFormAsk(request):
    username1 = request.user.username
    users = User.objects.get(username=username1)
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            subject = 'Your secret santa has a question for you!'
            message = form1.cleaned_data['question']
            recipient = [users.profile.AssignedEmail]
            send_mail(subject, message, 'hiscockssecretsanta@gmail.com', recipient)
            return redirect('profile')
            messages.info(request, 'Your email has been sent!')


    else:
        form1 = ContactForm()
        return render(request, 'users/askquestion.html', {'form1': form1})

def ContactFormReply(request):
    username1 = request.user.username
    users = User.objects.get(username=username1)
    if request.method == 'POST':
        form2 = ContactForm(request.POST)
        if form2.is_valid():
            subject = 'Your secret santa has a question for you!'
            message = form2.cleaned_data['question']
            recipient = [users.profile.SecretSantaEmail]
            send_mail(subject, message, 'hiscockssecretsanta@gmail.com', recipient)
            return redirect('profile')
            messages.info(request, 'Your email has been sent!')
    else:
        form2 = ContactForm()
        return render(request, 'users/replyquestion.html', {'form2': form2})

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