# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import gearman
import logging
from django_gearman_commands import GearmanServerInfo

log = logging.getLogger(__name__)

class Command(BaseCommand):
    """Pprint overview of Gearman server status and workers."""

    help = 'Print overview of Gearman server status and workers.'

    def handle(self, *args, **options):
        result = ''
        for server in settings.GEARMAN_SERVERS:
            server_info = GearmanServerInfo(server)
            result += server_info.get_server_info()
            
        self.stdout.write(result)
