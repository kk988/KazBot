import operator
from model.Candle import Candle

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
        for c in list_of_candles:
            #self.check_for_missing_candles(c[0])
            self.data.append(Candle(c))
            
        self.data.sort(key=operator.attrgetter("start_time"))
            
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
    
    def get_granularity(self):
        return self.granularity