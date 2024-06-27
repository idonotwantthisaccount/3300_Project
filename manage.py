#3300_Project (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
#
#3300_Project is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#
#You should have received a copy of the license along with this
#work. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coloradosnow.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
