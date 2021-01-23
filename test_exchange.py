from unittest import TestCase
from exchange import ExchangeRate


class TestExchangeRate(TestCase):
    def test_sgd_to_usd(self):
        self.assertEqual(ExchangeRate.sgd_to_usd(1), 0.8)

    def test_usd_to_sgd(self):
        self.assertEqual(ExchangeRate.usd_to_sgd(1), 1.4)
