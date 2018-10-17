from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=32)
    mdp   = models.CharField(max_length=32)
    ip    = models.CharField(max_length=100)
    useragent = models.CharField(max_length=100)
    date  = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = "Login de connexion"
        ordering = ['ip']

    def __str__(self):
        return self.ip



class Contact(models.Model):
    mail = models.CharField(max_length=100)
    objet   = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    ip    = models.CharField(max_length=100)
    useragent = models.CharField(max_length=100)
    date  = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = "Contact-Mails"
        ordering = ['ip']

    def __str__(self):
        return self.ip
