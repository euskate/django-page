# Generated by Django 2.0.5 on 2018-12-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20181129_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadablefile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='forms', verbose_name='양식 파일'),
        ),
    ]