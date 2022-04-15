# Generated by Django 2.2.2 on 2022-03-04 20:18

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default5Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redate', models.DateField(default=datetime.datetime.now, verbose_name='推荐时间')),
            ],
            options={
                'verbose_name': '默认电影推荐',
                'verbose_name_plural': '默认电影推荐',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='评分')),
                ('ds', models.BigIntegerField(default=1646396324.0, verbose_name='时间戳')),
            ],
            options={
                'verbose_name': '用户评分',
                'verbose_name_plural': '用户评分',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default='', max_length=255, null=True, verbose_name='评论')),
                ('star', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='星级')),
                ('reviewtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='提交时间')),
            ],
            options={
                'verbose_name': '用户回执',
                'verbose_name_plural': '用户回执',
            },
        ),
        migrations.CreateModel(
            name='Top5Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0, verbose_name='评分')),
            ],
            options={
                'verbose_name': '用户推荐信息',
                'verbose_name_plural': '用户推荐信息',
            },
        ),
        migrations.CreateModel(
            name='Top5Recommend_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0, verbose_name='评分')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.MovieInfo', verbose_name='电影')),
            ],
            options={
                'verbose_name': '用户推荐信息表2',
                'verbose_name_plural': '用户推荐信息表2',
            },
        ),
    ]