# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.conf import settings
from django.test import TestCase
from django.core.cache import cache
import django_gearman_commands
import logging

log = logging.getLogger(__name__)

class GearmanCommandsTest(TestCase):

    def test_overview(self):
        call_command('gearman_overview')
    
    def test_worker_simple(self):
        # submit job
        call_command('gearman_submit_job', 'footest')
        
        # let the worker process the job
        call_command('gearman_worker_footest')

        # verify job was processed
        self.assertEqual(cache.get('footest'), u'I AM FOO !', 'Unexpected footest worker result')
