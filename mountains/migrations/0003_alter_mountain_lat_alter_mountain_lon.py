# 3300_Project
# (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
# This file is part of the 3300_Project and is licensed under the GNU Affero General Public License (AGPLv3).
# You may obtain a copy of the AGPLv3 license at <https://www.gnu.org/licenses/agpl-3.0.en.html>.
#
# This project uses weather data from Open-Meteo (<https://open-meteo.com/>),
# licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
# You can view the license at <https://creativecommons.org/licenses/by/4.0/>.
# Generated by Django 5.0.6 on 2024-06-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0002_mountain_lat_mountain_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
