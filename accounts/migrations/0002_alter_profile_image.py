# Generated by Django 3.2.6 on 2021-09-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(upload_to='profile_images/', verbose_name='Profile Picture'),
        ),
    ]