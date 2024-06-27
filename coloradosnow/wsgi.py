# 3300_Project (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
#
# 3300_Project is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""
WSGI config for coloradosnow project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coloradosnow.settings')

application = get_wsgi_application()
