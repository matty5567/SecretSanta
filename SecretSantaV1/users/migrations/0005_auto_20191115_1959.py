# Generated by Django 2.2.7 on 2019-11-15 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191115_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Recipient',
            new_name='Assigned',
        ),
    ]