# Generated by Django 2.2.7 on 2019-11-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191115_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Gifter',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]