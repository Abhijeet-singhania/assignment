# Generated by Django 3.0.6 on 2021-09-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210905_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='username',
        ),
        migrations.AddField(
            model_name='items',
            name='userid',
            field=models.CharField(default='101', max_length=1000),
        ),
    ]
