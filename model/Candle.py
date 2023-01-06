

class Candle():
    def __init__(self, candle_info):
        if isinstance(candle_info, dict):
            candle_info = [
                candle_info['time'],
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