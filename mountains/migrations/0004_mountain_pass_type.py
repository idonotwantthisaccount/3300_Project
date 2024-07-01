# Generated by Django 5.0.6 on 2024-07-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0003_alter_mountain_lat_alter_mountain_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='pass_type',
            field=models.CharField(choices=[('epic', 'Epic Pass'), ('ikon', 'Ikon Pass'), ('other', 'Other')], default='unknown', max_length=10),
        ),
    ]
