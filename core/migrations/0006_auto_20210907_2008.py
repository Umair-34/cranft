# Generated by Django 3.2.6 on 2021-09-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210907_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
