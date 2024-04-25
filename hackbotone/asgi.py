"""
ASGI config for hackbotone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from juanjo1407.core.asgi import get_asgi_application

os.environ.setdefault('juanjo1407_SETTINGS_MODULE', 'hackbotone.settings')

application = get_asgi_application()
