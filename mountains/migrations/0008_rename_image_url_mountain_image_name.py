# Generated by Django 5.0.7 on 2024-07-15 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0007_alter_mountain_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mountain',
            old_name='image_url',
            new_name='image_name',
        ),
    ]
