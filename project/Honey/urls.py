from django.urls import path

from . import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),

    path('contact', views.contact, name='contact'),

    path('condition_utilisateur/', views.condition_user, name='condition_utilisateur'),

    path('donnees_perso/', views.donnees_perso, name='donnees_perso'),

    path('mentions_legales/', views.mentions_legales, name='mentions_legales'),

]
