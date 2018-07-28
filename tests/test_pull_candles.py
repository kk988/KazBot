from lib.Backtest import gdax_pull_candles, polo_pull_candles
import datetime
import math
import unittest

class TestCandles(unittest.TestCase):
    granularity = 900
    start = datetime.datetime(2018, 1, 1, 0, 0, 0)
    end = datetime.datetime(2018, 1, 31, 0, 0, 0)
    time_delta = end - start
    expected_num_of_candles = int(math.ceil(time_delta.total_seconds() / granularity))
    test_input = gdax_pull_candles( start, end, granularity )
    polo_test_input = polo_pull_candles(start, end, granularity)

    def test_gdax_candles(self):
        self.assertEqual(len(self.test_input), self.expected_num_of_candles)

    # Poloniex returns one extra candle
    def test_polo_candles(self):
        self.assertEqual(len(self.polo_test_input), self.expected_num_of_candles + 1)