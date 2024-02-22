"""
ASGI config for customer360 project.

It exposes the ASGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/

This ASGI (Asynchronous Server Gateway Interface) configuration file is used in Django projects
to define the ASGI application callable, which allows Django applications to handle asynchronous
requests, such as WebSockets, long polling, and other asynchronous tasks.

Configuration Details:
- This ASGI config file is specific to the 'customer360' Django project.
- The `application` variable is set to the ASGI callable, which is responsible for handling
  incoming ASGI messages and routing them to the appropriate Django application instance.
- The `get_asgi_application` function from `django.core.asgi` is used to get the ASGI application
  instance for the Django project.
- The `os.environ.setdefault` line sets the 'DJANGO_SETTINGS_MODULE' environment variable to
  'customer360.settings', indicating that this ASGI application should use the settings defined
  in 'customer360/settings.py'.

For more information on ASGI and its usage in Django, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to 'customer360.settings'
# This indicates that this ASGI application should use the settings defined in 'customer360/settings.py'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer360.settings')

# Get the ASGI application for the Django project
application = get_asgi_application()
