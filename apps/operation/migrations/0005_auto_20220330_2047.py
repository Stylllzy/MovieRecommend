# Generated by Django 2.2.2 on 2022-03-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20220327_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ds',
            field=models.BigIntegerField(default=1648644461.0, verbose_name='时间戳'),
        ),
    ]
