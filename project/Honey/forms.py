from django import forms
from .models import User
from .models import Contact

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'login','mdp'}
        widgets = {'mdp': forms.PasswordInput(),}



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['mail','objet','contenu']
        #widgets = {'ip': forms.HiddenInput(),'useragent': forms.HiddenInput(),'date': forms.HiddenInput()}
