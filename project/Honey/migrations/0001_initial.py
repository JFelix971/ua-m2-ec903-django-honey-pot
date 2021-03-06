# Generated by Django 2.1.1 on 2018-10-16 02:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=100)),
                ('objet', models.CharField(max_length=100)),
                ('contenu', models.TextField(null=True)),
                ('ip', models.CharField(max_length=100)),
                ('useragent', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Envoie Mail',
                'ordering': ['ip'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=32)),
                ('mdp', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=100)),
                ('useragent', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Login de connexion',
                'ordering': ['login'],
            },
        ),
    ]
