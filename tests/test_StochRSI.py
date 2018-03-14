import unittest
from Strategies.StochRSI import StochRSI
from exchanges.gdax import CandleList

def load_comma_delim_list(in_file):
    test_input = list()
    with open(in_file) as f:
        for inline in f:
            test_input.append(inline.rstrip().split(","))
    return test_input

class TestStochRSI(unittest.TestCase):
    FILE_DIR = "files/StochRSI"
    def test_init(self):
        test_input = load_comma_delim_list("/".join([self.FILE_DIR,"StochRSI_input.txt"]))
        expected_stoch_rsi = load_comma_delim_list("/".join([self.FILE_DIR,"StochRSI_expected.txt"]))
        
        test_input = [ map(float, x) for x in test_input ]
        expected_stoch_rsi = [ map(float, x) for x in expected_stoch_rsi ] 

        test_candles = CandleList(test_input, 900)
        
        test_Stoch_RSI = StochRSI(test_candles, 14)
        my_vals = test_Stoch_RSI.get_stoch_rsi_vals()

        rnd_my_vals = [[x[0], round(x[1], 10)] for x in my_vals]
        expected_output = [[x[0], round(x[1], 10)] for x in expected_stoch_rsi]
        
        self.assertEqual(rnd_my_vals,expected_output)