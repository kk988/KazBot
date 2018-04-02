from Strategies.StrategyManager import run_strategy
from Strategies.Trader import Trader  
from Strategies.Account import Account
from Strategies.Simulation import Simulation
from exchanges.gdax import CandleList
import datetime
import iso8601
import math
import gdax
import time

#usage of pull data
#test_input=pull_candles( datetime(2018, 2, 1, 0, 0, 0), datetime(2018, 2, 2, 0, 0, 0), 300)

class Backtest():
    def __init__(self, start, end, granularity, strategy, share_trade_ratio, **kwargs):
        # Pull data
        # Not sure if I'll need to save this.
        data = pull_candles(iso8601.parse_date(start), iso8601.parse_date(end), granularity)
        if not data:
            # something went wrong. create error and exit
            raise RuntimeError('Something went wrong pulling data for backtest') 
        
        data = [ x for x in data if x[0] >= int(iso8601.parse_date(start).strftime('%s')) ]

        self.candle_list = CandleList(data, granularity)
        self.granularity = granularity
        
        if not kwargs:
            kwargs = {}
        
        self.kwargs = kwargs
        
        #run strategy, returns trading calls
        
        self.strategy = run_strategy(strategy, self.candle_list, **kwargs)
        
        # Run simulation on account.
        account = Account(100)
        self.sim = Simulation(self.candle_list, self.strategy, account, share_trade_ratio)
        
    def generate_result_summary(self):
        print "\n--------------------"
        print "Backtest Results"
        print "--------------------"
        print "\nStart Time:", self.sim.get_start_datetime()
        print "End Time:", self.sim.get_end_datetime()
        print "\nStart Value:", self.sim.get_start_value()
        print "End Value:", self.sim.get_end_value()
        print "Value Change:", self.sim.get_value_change()
        print "\nStart Price:", self.sim.get_start_price()
        print "End Price:", self.sim.get_end_price()
        print "Price Change:", self.sim.get_price_change()
        
        print "\nGranularity:", self.granularity
        if self.kwargs:
            for (key, value) in self.kwargs.iteritems():
                print ": ".join([str(key), str(value)])
        print "Value Change Percent:", self.sim.get_value_change_percent() * 100, "%"
        print "Price Change Percent:", self.sim.get_price_change_percent() * 100, "%"
        print "Trades: ", self.sim.get_trades()
        
def pull_candles( start, end, granularity):
    # Get total number of candles
    total_candles = (end - start).total_seconds() / granularity
    
    # If candles > GDAX total (350) iterate over the endpoint
    # to gather all the candles that we can. 
    query_delay = 0.5
    gdax_max_candles = 300
    max_time_interval = datetime.timedelta(0,granularity * gdax_max_candles)
    required_requests = int(math.ceil(total_candles/gdax_max_candles))
    public_client = gdax.PublicClient()
    
    candle_data = list()
    curr_start = start
    for _ in range(0, required_requests):
        curr_end = curr_start + max_time_interval
        
        if curr_end > end:
            curr_end = end
        
        #max queries is 1 per 4 seconds
        time.sleep(query_delay)
        print "Pulling candle from", curr_start, "to", curr_end
        response_list = public_client.get_product_historic_rates('LTC-USD', start=curr_start, end=curr_end, granularity=granularity)
        if not isinstance(response_list, list):
            print "UH OH: " + response_list['message'] + "\n"
        candle_data.extend(response_list)
        curr_start = curr_end
            
    return sorted(candle_data)

