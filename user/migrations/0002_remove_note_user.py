# Generated by Django 4.0.3 on 2022-03-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]