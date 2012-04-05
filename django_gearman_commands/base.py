# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
import time
import gearman
import logging

log = logging.getLogger(__name__)

class HookedGearmanWorker(gearman.GearmanWorker):

    def __init__(self, exit_after_job, host_list=None):
        super(HookedGearmanWorker, self).__init__(host_list=host_list)
        self.exit_after_job = exit_after_job
        
    def after_job(self):
        return (not self.exit_after_job)
    
class GearmanWorkerBaseCommand(BaseCommand):
    """Base command for Gearman workers."""

    @property
    def task_name(self):
        """Override task_name property in worker to indicate what task should be registered in Gearman."""
        raise NotImplementedError, 'task_name should be implemented in worker'

    @property
    def exit_after_job(self):
        """Return True if worker should exit after processing job. False by default.

        You do not need to override this in standard case, except in case
        you want to control and terminate worker after processing jobs.
        Used by test worker 'footest'.

        """
        return False

    def do_job(self, job_data):
        """Gearman job execution logic.
        
        Override this in worker to perform job.
        
        """
        raise NotImplementedError, 'do_job() should be implemented in worker'
    
    def handle(self, *args, **options):
        try:
            worker = HookedGearmanWorker(exit_after_job=self.exit_after_job, host_list=settings.GEARMAN_SERVERS)
            log.info('Registering gearman task: %s', self.task_name)
            worker.register_task(self.task_name, self._invoke_job)
        except:
            log.exception('Problem with registering gearman task')
            raise
        
        worker.work()

    def _invoke_job(self, worker, job):
        """Invoke gearman job.
        
        Honestly, wrapper for do_job().
        
        """
        try:
            # represent default job data '' as None
            job_data = job.data if job.data else None
            self.stdout.write('Invoking gearman job, task: %s.\n' % self.task_name)

            result = self.do_job(job_data)

            log.info('Job finished, task: %s', self.task_name)
            self.stdout.write('Job finished, task: %s\n' % self.task_name)
            
            if result is not None:
                log.info(result)
                self.stdout.write('%s\n' % result)

            return 'OK'
        except:
            log.exception('Error occured when invoking job, task: %s', self.task_name)
            raise


    
