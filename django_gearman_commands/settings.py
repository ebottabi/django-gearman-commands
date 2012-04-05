from django.conf import settings

# gearman jobs servers
GEARMAN_SERVERS = getattr(settings, 'GEARMAN_SERVERS', ['127.0.0.1:4730'])
