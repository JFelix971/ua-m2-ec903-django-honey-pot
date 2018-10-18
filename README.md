Ce projet a été réalisé avec la collaboration de Anthony TEMMEL.

Le but de ce TP a été de réaliser un HoneyPot, afin de garder en mémoire les actions de chaque utilisateur.

__**Pré-requis du déploiement du Site**__
 -  Installer python 3:
  ```sh
 $ sudo apt-get update
 $ sudo apt-get install python3.6
 ```
 -  Création d'un dossier qui va nous servir de support et accéder à ce dossier
 ```sh
$ mkdir HoneyPot
$ cd HoneyPot
```
 -  Création d'un environnement virtuel et accès à l'environnement virtuel
  ```sh
$ virtualenv -p pyhton3 venv
$ . venv/bin/activate
```
 -  Installation de django
  ```sh
$ pip3 install django
```

**Site**
 -  Récupération du git
  ```sh
$ git clone https://github.com/JFelix971/ua-m2-ec903-django-honey-pot.git
```
 -  Accéder au projet
  ```sh
$ cd ua-m2-ec903-django-honey-pot/project/
```
 -  Création de la base de données et du superuser(admin) :
   ```sh
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
```
  - Lancement du serveur local
   ```sh
$ python3 manage.py runserver
```



 


