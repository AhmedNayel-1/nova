# Generated by Django 3.1.2 on 2020-11-24 14:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novav1', '0016_order_balls'),
    ]

    operations = [
        migrations.CreateModel(
            name='statue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statue', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.TextField()),
                ('Calldate', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('Followup', models.IntegerField(choices=[(180, '6اشهر'), (365, 'سنه'), (730, 'سنتين')], default=365)),
                ('FollowupDate', models.DateField(default=datetime.datetime.now)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novav1.patient')),
                ('Statue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.statue')),
            ],
        ),
    ]
