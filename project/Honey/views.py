from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, ContactForm
from .models import User, Contact

import datetime

# Create your dviews here.
def acceuil(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        user = User()
        user.login = form.cleaned_data['login']
        user.mdp = form.cleaned_data['mdp']

        user.useragent = request.META['HTTP_USER_AGENT']
        user.date = datetime.datetime.now()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        user.ip = ip

        user.save()


    return render(request,'Honey/acceuil.html',locals())


def contact(request):
    form = ContactForm(request.POST)

    if form.is_valid():
       contact = Contact()

       contact.mail = form.cleaned_data['mail']

       contact.objet = form.cleaned_data['objet']

       contact.contenu = form.cleaned_data['contenu']

       contact.useragent = request.META['HTTP_USER_AGENT']

       contact.date = datetime.datetime.now()

       x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

       if x_forwarded_for:
           ip = x_forwarded_for.split(',')[0]
       else:
           ip = request.META.get('REMOTE_ADDR')

       contact.ip = ip

       contact.save()
       ##envoi = True

    return render(request,'Honey/contact.html', locals())


def condition_user(request):
    return render(request,'Honey/condition_user.html', locals())

def donnees_perso(request):
    return render(request,'Honey/donnees_perso.html', locals())

def mentions_legales(request):
    return render(request,'Honey/mentions_legales.html', locals())
