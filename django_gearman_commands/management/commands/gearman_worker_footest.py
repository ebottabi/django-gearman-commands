# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.cache import cache
import django_gearman_commands
import logging

log = logging.getLogger(__name__)

class Command(django_gearman_commands.GearmanWorkerBaseCommand):
    """Base command for Gearman workers."""
    
    @property
    def task_name(self):
        return 'footest'

    @property
    def exit_after_job(self):
        return True # terminate after job is handled. Do not do this for standard workers !
    
    def do_job(self, job_data):
        # set data to cache
        cache.set('footest', u'I AM FOO !')
        

    

    
