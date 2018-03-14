import unittest
from exchanges.gdax import CandleList
from Strategies import RSI

def load_comma_delim_list(in_file):
    test_input = list()
    with open(in_file) as f:
        for inline in f:
            test_input.append(inline.rstrip().split(","))
    return test_input

class TestRSI(unittest.TestCase):
    FILE_DIR = "files/RSI"
    
    def test_init(self):
        test_input = load_comma_delim_list("/".join([self.FILE_DIR,"RSI_init_input.txt"]))
        expected_rsi = load_comma_delim_list("/".join([self.FILE_DIR,"RSI_init_expected.txt"]))
        
        test_input = [ map(float, x) for x in test_input ]
        expected_rsi = [ map(float, x) for x in expected_rsi ] 
    
        # Setup Candles (graularity of input is 900 sec)
        test_candles = CandleList(test_input, 900)
        
        # Run RSI
        my_rsi = RSI.RSI(test_candles, 14)
        my_vals = my_rsi.get_calculated_rsi_vals()
        rnd_my_vals = [[x[0], round(x[1], 8)] for x in my_vals]
        
        self.assertEqual(rnd_my_vals, expected_rsi)
        
    def test_calc_rsi(self):
        test_inputs = load_comma_delim_list("/".join([self.FILE_DIR, "calc_rsi_input.txt"]))
        expected_outs = load_comma_delim_list("/".join([self.FILE_DIR, "calc_rsi_expected.txt"])).pop()
        
        for x in range(len(test_inputs)):
            (avg_gains, avg_losses) = map(float, test_inputs[x])
            rsi_val = RSI.calc_rsi(avg_gains, avg_losses)
            self.assertEqual(round(rsi_val, 8), float(expected_outs[x]))
        
    

if __name__ == '__main__':
    unittest.main()