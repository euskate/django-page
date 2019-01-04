# Generated by Django 2.0.5 on 2018-12-08 11:18

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20181202_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='슬라이드 순서')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(help_text='슬라이드 이미지', upload_to='slide')),
                ('title', models.CharField(max_length=40, verbose_name='제목')),
                ('subtitle', models.CharField(max_length=100, verbose_name='부제목')),
                ('description', models.TextField(blank=True, null=True, verbose_name='추가설명')),
                ('delay', models.PositiveIntegerField(default=12, verbose_name='표시시간')),
                ('button_label', models.CharField(blank=True, max_length=40, null=True, verbose_name='버튼 이름 제목')),
                ('button_link', models.URLField(blank=True, null=True, verbose_name='버튼 링크')),
            ],
            options={
                'verbose_name': '슬라이드',
                'verbose_name_plural': '슬라이드 목록',
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='page',
            name='theme',
        ),
        migrations.AlterField(
            model_name='page',
            name='featured',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='이미지 추가 시 페이지 상단에 이미지 타이틀이 표시 됩니다.', null=True, upload_to='featured', verbose_name='타이틀 이미지'),
        ),
        migrations.AddField(
            model_name='slide',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='page.Page'),
        ),
    ]