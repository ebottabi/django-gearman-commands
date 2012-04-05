# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import gearman
import logging

log = logging.getLogger(__name__)

class Command(BaseCommand):
    """Submit specific gearman job with job data as an arguments."""

    args = '<task_name> [job_data]'
    help = 'Submit gearman job with specified task, optionally with job data'

    def handle(self, *args, **options):
        try:
            task_name = None
            job_data = ''

            if len(args) == 0:
                raise CommandError('At least task name must be provided.')

            task_name = args[0]
            if len(args) > 1:
                job_data = args[1]

            self.stdout.write('Submitting job: %s, job data: %s.\n' % (task_name, job_data if job_data else '(empty)'))

            client = gearman.GearmanClient(settings.GEARMAN_SERVERS)
            result = client.submit_job(task_name, job_data, wait_until_complete=False, background=True)
            
            self.stdout.write('Job submission done, result: %s.\n' % result)
        except:
            log.exception('Error when submitting gearman job')
            raise
