# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from prettytable import PrettyTable
import gearman
import logging

log = logging.getLogger(__name__)

class Command(BaseCommand):
    """Pretty-print overview of Gearman server status and workers."""

    help = 'Print overview of Gearman server status and workers.'

    def handle(self, *args, **options):
        client = gearman.GearmanAdminClient(settings.GEARMAN_SERVERS)
                
        # get server version
        version = client.get_version()

        table = PrettyTable(['Gearman Server Version'])
        table.add_row([version])
        
        self.stdout.write('%s.\n\n' % table)

        # status
        raw_status = client.get_status()
        table = PrettyTable(['Task Name', 'Total Workers', 'Running Jobs', 'Queued Jobs'])
        for r in raw_status:
            table.add_row([r['task'], r['workers'], r['running'], r['queued']])

        self.stdout.write('%s.\n' % table)

        # TODO: workers
