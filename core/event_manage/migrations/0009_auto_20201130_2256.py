# Generated by Django 3.1.2 on 2020-11-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_manage', '0008_auto_20201130_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='Presence',
        ),
        migrations.AddField(
            model_name='events',
            name='arrivetime2',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
