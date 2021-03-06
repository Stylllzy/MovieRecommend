# Generated by Django 2.2.2 on 2022-03-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220327_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=7, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='大学生男.png', null=True, upload_to='http://127.0.0.1:8080/media/', verbose_name='头像'),
        ),
    ]
