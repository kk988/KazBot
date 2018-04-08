from datetime import datetime

# Note: Ways to change out of ISO-8601:
# datetime.datetime.strptime("2014-11-06T10:34:47.123456Z", "%Y-%m-%dT%H:%M:%S.%fZ")
# iso8601.parse("2014-11-06T10:34:47.123456Z")

# List of candles should be an list of Candle objects
class CandleList():
    def __init__(self, list_of_candles=None, granularity=None):
        self.data = list()
        self.granularity = granularity
        
        if list_of_candles:
            self.populate_data(list_of_candles)
        
    def add_candle(self, candle_obj):
        #self.check_for_missing_candles(candle_obj.get_start_time())
        self.data.append(candle_obj)
    
    def populate_data(self, list_of_candles):
        # check for missing candles
        for c in sorted(list_of_candles):
            #self.check_for_missing_candles(c[0])
            self.data.append(Candle(c))
            
    # Append empty candles for any time 
    def check_for_missing_candles(self,new_start_time):
        if not self.data:
            return
        next_calc_time = self.data[-1].get_start_time() + self.granularity
        while next_calc_time < new_start_time:
            price = self.data[-1].get_close_price()
            self.data.append(Candle([next_calc_time, price, price, price, price, 0]))
            next_calc_time += self.granularity
        return
    
    def get_candle_list(self):
        return self.data
    
class Candle():
    def __init__(self, candle_info):
        if isinstance(candle_info, dict):
            candle_info = [
                candle_info['date'],
                candle_info['low'],
                candle_info['high'],
                candle_info['open'],
                candle_info['close'],
                candle_info['volume']
                ]
        
        
        self.start_time = candle_info[0]
        self.low = float(candle_info[1])
        self.high = float(candle_info[2])
        self.open_price = float(candle_info[3])
        self.close_price = float(candle_info[4])
        self.volume = float(candle_info[5])
        self.set_gain_loss()
        
    def set_gain_loss(self):
        delta_price = self.close_price - self.open_price
        if delta_price > 0:
            self.gain = delta_price
            self.loss = 0
        else:
            self.gain = 0
            self.loss = abs(delta_price)
    
    def get_start_time(self):
        return self.start_time
    
    def get_low(self):
        return self.low
    
    def get_high(self):
        return self.high
    
    def get_open_price(self):
        return self.open_price
    
    def get_close_price(self):
        return self.close_price
    
    def get_volume(self):
        return self.volume
    
    def get_gain(self):
        return self.gain
    
    def get_loss(self):
        return self.loss