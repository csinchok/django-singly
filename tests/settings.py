import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'app_name',
)

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
TEST_DISCOVERY_ROOT = os.path.join(BASE_PATH, 'tests')

TEST_RUNNER = 'tests.runner.DiscoveryDjangoTestSuiteRunner'

FIXTURE_DIRS = (
    os.path.join(TEST_DISCOVERY_ROOT, 'fixtures'),
)
