# Generated by Django 5.0.6 on 2024-06-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='lat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mountain',
            name='lon',
            field=models.IntegerField(null=True),
        ),
    ]
