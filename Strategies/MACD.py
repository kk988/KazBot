from Strategies.EMA import EMA
from operator import indexOf
import operator
from Strategies.TradeAction import TradeAction
from Strategies.TraderTools import *

class MACD():
    def __init__(self, data):
        self.data = data
        self.ema_26 = EMA(data, 26).get_results()
        self.ema_12 = EMA(data, 12).get_results()
        self.macd = {x[0]: x[1] for x in calc_macd(self.ema_12, self.ema_26)}
        self.signal = {x[0]: x[1] for x in EMA(self.macd, 9).get_results()}
        self.run()
        
    def run(self):
        self.histogram = dict()
        
        for k in self.signal:
            self.histogram[k] =  self.macd[k] - self.signal[k]
            
    def get_signal(self, time):
        if not time in self.histogram:
            raise IndexError("Time provided not in MACD signal list.")
            
            return False
        else:
            return self.signal[time]
        
    def is_histogram_change(self, time, granularity):
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
            
    def is_MACD_change(self, time, granularity):
        prev_time = time - granularity
        
        if not (time in self.macd and prev_time in self.macd):
            return 0
        else:
            prev_signal = self.macd[prev_time]
            curr_signal = self.macd[time]
            
            prev_sign = prev_signal / abs(prev_signal)
            curr_sign = curr_signal / abs(curr_signal)
            
            if prev_sign + curr_sign == 0:
                return curr_sign
            else:
                return 0
    
    def get_histogram(self):
        return self.histogram
    
class Trader():
    STOP_FACTOR = 2
    AVG_CANDLE_PERIOD = 14
    
    def __init__(self, data):
        self.candle_list_obj = data
        self.data = data.get_candle_list()
        self.granularity = self.data[1].get_start_time() - self.data[0].get_start_time()
        self.macd_obj = MACD(data)
        self.macd_histo = self.macd_obj.get_histogram()
        self.stop = None
        self.target = None
        self.run()
        
    def run(self):
        self.actions = []
        for candle in self.data:
            time = candle.get_start_time()
            histo_change = None
            macd_change = None
            
            if time in self.macd_histo:
                histo_change = self.macd_obj.is_histogram_change(time, self.granularity)
                macd_change = self.macd_obj.is_MACD_change(time, self.granularity)
                
            if histo_change or macd_change:
                if histo_change > 0 or macd_change > 0:
                    self.actions.append(TradeAction(time, TradeAction.BUY))
                    variation = average_candle_length(self.candle_list_obj, time, self.AVG_CANDLE_PERIOD) * self.STOP_FACTOR
                    self.stop = candle.get_low() - variation
                    self.target = candle.get_high() + variation
                #else:
                    #self.actions.append(TradeAction(time, TradeAction.SELL))
                    #self.stop = None
                    #self.target = None
                    
            if self.stop or self.target:
                if self.stop >= candle.get_close_price():
                    self.actions.append(TradeAction(time, TradeAction.SELL))
                    self.stop = None
                    self.target = None
                elif self.target <= candle.get_close_price():
                    self.actions.append(TradeAction(time, TradeAction.SELL))
                    self.stop = None
                    self.target = None
                else:
                    variation = average_candle_length(self.candle_list_obj, time, self.AVG_CANDLE_PERIOD) * self.STOP_FACTOR
                    self.stop = candle.get_low() - variation
                    self.target = candle.get_high() + variation
    
    def get_actions(self):
        return self.actions

def calc_macd(ema_12, ema_26):
    first_time = ema_26[0][0]
    print(first_time)
    first_i = indexOf([x[0] for x in ema_12], first_time)
    
    ema_12_no_time = [x[1] for x in ema_12[first_i:]]
    ema_26_no_time = [x[1] for x in ema_26]
    times = [x[0] for x in ema_26]
    macds_no_time = map(operator.sub, ema_12_no_time, ema_26_no_time)
    return [list(x) for x in zip(times, macds_no_time)]