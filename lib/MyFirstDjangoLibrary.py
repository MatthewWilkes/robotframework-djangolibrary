"""A library for testing Django with Robot Framework.
"""

from robot.api import logger

import os
import signal
import subprocess

ROBOT_LIBRARY_DOC_FORMAT = 'reST'


class MyFirstDjangoLibrary:

    django_pid = None
    selenium_pid = None

    # TEST CASE => New instance is created for every test case.
    # TEST SUITE => New instance is created for every test suite.
    # GLOBAL => Only one instance is created during the whole test execution.
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, host="127.0.0.1", port=8000):
        logger.info("INIT", also_console=True)
        self.host = host
        self.port = port

    def start_django(self):
        args = [
            'python',
            'mysite/manage.py',
            'runserver',
            '%s:%s' % (self.host, self.port),
            '--nothreading',
            '--noreload',
        ]
        self.app = subprocess.Popen(args)
        self.django_pid = self.app.pid
        logger.info(
            "Django started (PID: %s)" % self.app.pid,
        )

    def stop_django(self):
        os.kill(self.django_pid, signal.SIGKILL)
        logger.info(
            "Django stopped (PID: %s)" % self.django_pid,
        )

    def start_selenium(self):
        args = [
            'java',
            '-jar',
            '.env/lib/python2.7/site-packages/SeleniumLibrary/lib/selenium-server.jar',
        ]
        self.selenium_pid = subprocess.Popen(args).pid
        logger.info(
            "Selenium started (PID: %s)" % self.selenium_pid,
        )

    def stop_selenium(self):
        os.kill(self.selenium_pid, signal.SIGKILL)
        logger.info(
            "Selenium stopped (PID: %s)" % self.selenium_pid,
        )