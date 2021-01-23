import unittest
from exchange import ExchangeRate


class TestExchangeRate(unittest.TestCase):
    def setUp(self):
        self.er = ExchangeRate()


class TestInit(TestExchangeRate):
    def test_change_sgd(self):
        self.assertEqual(self.er.sgd_to_usd(1), 0.7)

    def test_change_use(self):
        self.assertEqual(self.er.usd_to_sgd(1), 1.4)
