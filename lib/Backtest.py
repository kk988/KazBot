from Strategies.StrategyManager import run_strategy
from Strategies import Trader  
import datetime
import iso8601
import math
import gdax
import time

#usage of pull data
#test_input=pull_candles( datetime(2018, 2, 1, 0, 0, 0), datetime(2018, 2, 2, 0, 0, 0), 300)

class Backtest():
    def __init__(self, start, end, granularity, strategy, **kwargs):
        # Pull data
        # Not sure if I'll need to save this.
        self.data = pull_candles(iso8601.parse_date(start), iso8601.parse_date(end), granularity)
        if not self.data:
            # something went wrong. create error and exit
            raise RuntimeError('Something went wrong pulling data for backtest') 
            
        #run strategy
        self.strategy = run_strategy(strategy, self.data, **kwargs)
        
        # use strategy output with exchange rules
        # Call trader to figure out buys/sells
        self.trading_calls = Trader(strategy)
        
        #self.results = generate_result_summary(trading_calls)
    
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