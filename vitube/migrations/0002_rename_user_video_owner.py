# Generated by Django 3.2 on 2022-12-21 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitube', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='user',
            new_name='owner',
        ),
    ]
