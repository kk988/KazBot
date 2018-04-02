from Strategies.EMA import EMA
from operator import indexOf
from _ast import operator
import operator

class MACD():
    def __init__(self, data):
        self.data = data
        self.ema_26 = EMA(data, 26).get_results()
        self.ema_12 = EMA(data, 12).get_results()
        self.macd = calc_macd(self.ema_12, self.ema_26)
        self.signal = EMA(self.macd, 9).get_results()
        self.run()
        
    def run(self):
        self.histogram = dict()
        first_i = indexOf([x[0] for x in self.macd], self.signal[0][0])
        
        for x, y in zip(self.macd[first_i:], self.signal):
            self.histogram[x[0]] =  x[1] - y[1]
            
    def get_signal(self, time):
        if not time in self.histogram:
            raise IndexError("Time provided not in MACD signal list.")
            
            return False
        else:
            return self.signal[time]
        
    def get_signal_change(self, time, granularity):
        prev_time = time - granularity
        
        if not (time in self.histogram and prev_time in self.histogram):
            return 0
        else:
            prev_signal = self.signal[prev_time]
            curr_signal = self.signal[time]
            
            prev_sign = prev_signal / abs(prev_signal)
            curr_sign = curr_signal / abs(curr_signal)
            
            if prev_sign + curr_sign == 0:
                return curr_sign
            else:
                return 0
    
    def get_histogram(self):
        return self.histogram

def calc_macd(ema_12, ema_26):
    first_time = ema_26[0][0]
    print first_time
    first_i = indexOf([x[0] for x in ema_12], first_time)
    
    ema_12_no_time = [x[1] for x in ema_12[first_i:]]
    ema_26_no_time = [x[1] for x in ema_26]
    times = [x[0] for x in ema_26]
    macds_no_time = map(operator.sub, ema_12_no_time, ema_26_no_time)
    return [list(x) for x in zip(times, macds_no_time)]