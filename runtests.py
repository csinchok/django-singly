#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

from django.test.utils import get_runner
from django.conf import settings


def runtests():
    TestRunner = get_runner(settings)

    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests([])
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
