# 3300_Project
# (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
# This file is part of the 3300_Project and is licensed under the GNU Affero General Public License (AGPLv3).
# You may obtain a copy of the AGPLv3 license at <https://www.gnu.org/licenses/agpl-3.0.en.html>.
#
# This project uses weather data from Open-Meteo (<https://open-meteo.com/>),
# licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
# You can view the license at <https://creativecommons.org/licenses/by/4.0/>.
"""
ASGI config for coloradosnow project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coloradosnow.settings')

application = get_asgi_application()
