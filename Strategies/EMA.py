from model.CandleList import CandleList
class EMA():
    def __init__(self, data, n_periods):
        self.data = parse_data(data)
        self.n_periods = n_periods
        self.run()
        
    def run(self):
        curr_vals = self.data[:self.n_periods]
        next_vals = self.data[self.n_periods:]
        
        sma = float(sum([x[1] for x in curr_vals])) / float(self.n_periods)
        curr_time = curr_vals[-1][0]
        multiplier = (2.0 / (self.n_periods + 1.0))
        print("Multiplier: ", multiplier)
        
        self.results = [[curr_time, sma]]
        
        ema = sma
        
        while next_vals:
            curr_candle = next_vals.pop(0)
            curr_price = float(curr_candle[1])
            curr_time = curr_candle[0]
            
            #EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day). 
            ema = (curr_price - ema) * multiplier + ema
            
            self.results.append([curr_time, ema])
            
    def get_results(self):
        return self.results

def parse_data(data):
    if isinstance(data, CandleList):
        candles = data.get_candle_list()
        
        return [[candle.get_start_time(), candle.get_close_price()] for candle in candles]
    elif isinstance(data, dict):
        return [[k,v] for k,v in data.items()]
    else:
        return data