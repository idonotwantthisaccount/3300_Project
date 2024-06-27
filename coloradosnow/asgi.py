# 3300_Project (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
#
# 3300_Project is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <https://creativecommons.org/licenses/by/4.0/>.
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
