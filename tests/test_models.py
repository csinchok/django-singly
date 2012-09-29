# -*- coding: utf-8 -*-
from django.test import TestCase

from app_name.models import MyModel


class MyTest(TestCase):
    fixtures = ['test_blah.json']

    def testBlahCount(self):
        """Test blah count."""
        blah_count = MyModel.objects.count()
        self.assertEqual(blah_count, 2)
