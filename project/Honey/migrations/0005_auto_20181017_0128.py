# Generated by Django 2.1.1 on 2018-10-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Honey', '0004_auto_20181017_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='objet',
            field=models.CharField(max_length=100),
        ),
    ]
