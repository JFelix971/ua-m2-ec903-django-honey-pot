from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, ContactForm

# Create your dviews here.
def acceuil(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)


    return render(request,'Honey/acceuil.html',{'form':form})


def condition_user(request):
    return render(request,'Honey/condition_user.html')

def donnees_perso(request):
    return render(request,'Honey/donnees_perso.html')

def mentions_legales(request):
    return render(request,'Honey/mentions_legales.html')
