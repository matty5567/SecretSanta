# Generated by Django 2.2.7 on 2019-11-15 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191115_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Gifter',
            new_name='SecretSanta',
        ),
    ]
