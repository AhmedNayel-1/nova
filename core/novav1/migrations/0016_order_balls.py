# Generated by Django 3.1.2 on 2020-11-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0015_auto_20201119_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='balls',
            field=models.IntegerField(default=0),
        ),
    ]
