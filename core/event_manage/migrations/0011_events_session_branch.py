# Generated by Django 3.1.2 on 2020-12-01 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0027_auto_20201202_0148'),
        ('event_manage', '0010_auto_20201201_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='session_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.branch'),
        ),
    ]