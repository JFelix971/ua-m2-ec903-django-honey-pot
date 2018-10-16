from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

# Create your dviews here.
def acceuil(request):
    form = LoginForm(request.POST)
##    if request.form == 'POST':
##        if form.is_valid():
##            user = form.save(commit=False)


    return render(request,'Honey/acceuil.html',{'form':form})
