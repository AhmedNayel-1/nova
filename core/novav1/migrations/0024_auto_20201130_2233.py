# Generated by Django 3.1.2 on 2020-11-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0023_auto_20201130_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='8ZHUJRPMEDHOIE44GFB4', max_length=20),
        ),
    ]
