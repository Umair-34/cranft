# Generated by Django 3.2.6 on 2021-09-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover_images/', verbose_name='Cover Picture'),
        ),
    ]
