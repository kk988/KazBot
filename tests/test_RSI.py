import unittest
from exchanges.gdax import CandleList
from Strategies import RSI

def load_comma_delim_list(in_file):
    test_input = list()
    with open(in_file) as f:
        for inline in f:
            test_input.append(map(float, inline.rstrip().split(",")))
    return test_input

class TestRSI(unittest.TestCase):
    
    def testCalculations(self):
        test_input = load_comma_delim_list("files/RSI_input.txt")
        expected_rsi = load_comma_delim_list("files/RSI_expected.txt")
    
        # Setup Candles (graularity of input is 900 sec)
        test_candles = CandleList(test_input, 900)
        
        # Run RSI
        my_rsi = RSI.RSI(test_candles, 14)
        my_vals = my_rsi.get_calculated_rsi_vals()
        rnd_my_vals = [[x[0], round(x[1], 8)] for x in my_vals]
        
        self.assertEqual(rnd_my_vals, expected_rsi)

if __name__ == '__main__':
    unittest.main()