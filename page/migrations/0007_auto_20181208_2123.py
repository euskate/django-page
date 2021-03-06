# Generated by Django 2.0.5 on 2018-12-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20181208_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ['order'], 'verbose_name': '슬라이드', 'verbose_name_plural': '슬라이드'},
        ),
        migrations.AlterField(
            model_name='slide',
            name='button_label',
            field=models.CharField(blank=True, help_text='공백인 경우 버튼이 표시 되지 않음', max_length=40, null=True, verbose_name='버튼 이름 제목'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='delay',
            field=models.PositiveIntegerField(default=12, help_text='슬라이드가 표시되는 시간(초)', verbose_name='표시시간'),
        ),
    ]
