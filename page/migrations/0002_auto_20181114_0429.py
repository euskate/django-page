# Generated by Django 2.0.5 on 2018-11-13 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='summery',
            new_name='summary',
        ),
    ]
