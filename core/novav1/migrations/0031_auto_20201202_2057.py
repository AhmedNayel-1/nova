# Generated by Django 3.1.2 on 2020-12-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0030_auto_20201202_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='NQQKJ2LG2IZ7AW49ZC48', max_length=20),
        ),
    ]