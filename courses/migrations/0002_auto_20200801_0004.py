# Generated by Django 3.0.8 on 2020-07-31 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='tittle',
            new_name='title',
        ),
    ]
