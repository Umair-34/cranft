# Generated by Django 3.2.6 on 2021-09-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Tagline',
            field=models.TextField(blank=True, null=True),
        ),
    ]
