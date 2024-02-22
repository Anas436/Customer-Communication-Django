#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the Django settings module for the command-line utility
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer360.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle import error if Django is not installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute Django commands from the command line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
