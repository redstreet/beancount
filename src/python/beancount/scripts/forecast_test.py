import unittest

import beancount.scripts.forecast  # Register the plugin.
from beancount.loader import loaddoc
from beancount import loader


def tearDown():
    loader.uninstall_load_filter(
        beancount.scripts.forecast.forecast_filter)


class TestScriptForecast(unittest.TestCase):

    @loaddoc
    def test_success(self, entries, errors, options):
        """
        2011-01-01 open Expenses:Restaurant
        2011-01-01 open Assets:Cash

        2011-05-17 # "Something [MONTHLY]"
          Expenses:Restaurant   50.02 USD
          Assets:Cash
        """
        self.assertLessEqual(3, len(entries))
