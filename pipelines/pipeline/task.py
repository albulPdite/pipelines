import logging
from copy import copy

EXECUTION_SUCCESSFUL = 0
EXECUTION_FAILED = 1

log = logging.getLogger('pipelines')


class Task(object):

    def __init__(self, name, executor, args, always_run, ignore_errors,
                 timeout):
        self.name = name
        self.executor = executor
        self.args = args
        self.always_run = always_run
        self.ignore_errors = ignore_errors
        self.timeout = timeout

    @staticmethod
    def from_dict(task_dict):
        task_args = copy(task_dict)
        executor = task_args.pop('type')

        name = ''
        if 'name' in task_dict:
            name = task_dict.pop('name')

        always_run = False
        if 'always_run' in task_dict:
            always_run = task_dict.pop('always_run')

        ignore_errors = False
        if 'ignore_errors' in task_dict:
            ignore_errors = task_dict.pop('ignore_errors')

        timeout = False
        if 'timeout' in task_dict:
            timeout = task_dict.pop('timeout')

        return Task(name, executor, task_args, always_run, ignore_errors,
                    timeout)


class TaskResult(dict):

    def __init__(self, status, message='', data={}, return_obj={}):
        self['status'] = status
        self['message'] = message
        self['data'] = data
        self['return_obj'] = return_obj

    @property
    def status(self):
        return self.get('status')

    @property
    def message(self):
        return self.get('message')

    @property
    def data(self):
        return self.get('data')

    @property
    def return_obj(self):
        return self.get('return_obj')

    def is_successful(self):
        return self.status == EXECUTION_SUCCESSFUL
