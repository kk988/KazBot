from exchanges.gdax import CandleList
from Strategies.TradeAction import TradeAction

class RSI():
    def __init__ (self,list_of_candles, n_periods):
        self.vals = list()
        self.calculate_vals(list_of_candles.get_candle_list(),n_periods)
            
    def calculate_vals(self,candle_list, n_periods):
        (gains, losses) = pull_gains_and_losses(candle_list[:n_periods])
               
        #first generate the first
        avg_gains = sum(gains) / n_periods
        avg_losses = sum(losses) / n_periods
        
        self.vals.append([candle_list[n_periods-1].get_start_time() , self.calc_rsi(avg_gains, avg_losses)])

        for i in range(n_periods, len(candle_list)):
            (cur_gain,cur_loss) = pull_gains_and_losses([candle_list[i]])
            avg_gains = (avg_gains * (n_periods-1) + cur_gain[0]) / n_periods
            avg_losses = (avg_losses * (n_periods-1) + cur_loss[0]) / n_periods
            
            self.vals.append([candle_list[i].get_start_time(), self.calc_rsi(avg_gains, avg_losses)])
            
    def get_calculated_rsi_vals(self):
        return self.vals
    
    def calc_rsi(self, avg_gains, avg_losses):
        RS = avg_gains/avg_losses
        return 100 - (100/(1+RS))
        
class Trader():
    UP = 1
    DOWN = -1
    OVERBOUGHT = "OVERBOUGHT"
    OVERSOLD = "OVERSOLD"
    
    def __init__(self, candle_list, rsi_obj, swing_period):
        self.candle_list = candle_list
        self.candles = self.candle_list.get_candle_list()
        self.swing_period = swing_period
        self.swing_high = None
        self.swing_low = None
        self.risk = None
        self.target = None
        self.breakeven = None
        self.stop = None
        self.rsi_status = False
        self.direction = None
        self.take_action = False
        self.rsi_vals = rsi_obj.get_calculated_rsi_vals()
        self.run_actions()
    
    def get_actions(self):
        return self.actions
    
    def swing_range(self, curr_i):
        return self.candles[curr_i - (self.swing_period * 2) + 1: curr_i + 1]
    
    def set_swing_low(self, curr_time):
        curr_i = index_of_time(self.candle_list, curr_time)
        swing_range = self.swing_range(curr_i)
        
        self.swing_low = min([x.get_close_price() for x in swing_range])
        
    def set_swing_high(self, curr_time):
        curr_i = index_of_time(self.candle_list, curr_time)
        swing_range = self.swing_range(curr_i)
        
        self.swing_high = max([x.get_close_price() for x in swing_range])
        
    def run_actions(self):
        
        #get starting index for both condles and rsi
        start_i = self.swing_period * 2
        swing_start_time = self.candles[start_i].get_start_time()
        rsi_start_time = self.rsi_vals[0][0]
        max_start_time = max([swing_start_time, rsi_start_time])
        candle_i = index_of_time(self.candle_list, max_start_time)
        rsi_i = index_of_time(self.rsi_vals, max_start_time)
        
        #TODO add HOLD actions until enough data to make decision
        actions = []
        
        for candle in self.candles[candle_i:]:
            curr_rsi = self.rsi_vals[rsi_i][1]
            
            #take action from previous iteration's decisions
            if self.take_action:
                actions.append(TradeAction(candle.get_start_time(), self.take_action[0], self.take_action[1]))            
                self.take_action = None
            
            #if already predicting direction, determine if exit is necessary
            if self.direction:
                curr_price = candle.get_close_price()
                
                if self.direction == self.DOWN:
                    if curr_price >= self.stop:
                        #abandon the down trend
                        self.direction = None
                    elif not self.stop == self.breakeven and curr_price <= self.breakeven - (self.risk * 0.5):
                        #not sure if we should buy here
                        #at 50% of risk, redefine exit
                        self.stop = self.breakeven
                    elif is_oversold(curr_rsi):
                        #exit current trend
                        self.direction = None
                        
                elif self.direction == self.UP:
                    if curr_price <= self.stop:
                        self.direction = None
                    elif not self.stop == self.breakeven and curr_price >= self.breakeven + (self.risk * 0.5):
                        #self.take_action = [TradeAction.SELL, 0.5]
                        self.stop = self.breakeven
                    elif is_overbought(curr_rsi):
                        self.direction = None
                        
            elif self.rsi_status:
                if self.rsi_status == self.OVERBOUGHT:
                    if not is_overbought(curr_rsi) and candle.get_open_price() > candle.get_close_price():
                        self.direction = self.DOWN
                        self.set_swing_high(candle.get_start_time())
                        self.breakeven = candle.get_close_price()
                        self.risk = abs(self.swing_high - self.breakeven)
                        self.stop = self.swing_high
                        self.take_action = [TradeAction.SELL, 1]
                elif self.rsi_status == self.OVERSOLD:
                    if not is_oversold(curr_rsi) and candle.get_open_price() < candle.get_close_price():
                        self.direction = self.UP
                        self.set_swing_low(candle.get_start_time())
                        self.breakeven = candle.get_close_price()
                        self.risk = abs(self.breakeven - self.swing_low)
                        self.stop = self.swing_low
                        self.take_action = [TradeAction.BUY, 1]
            
            #reset for next iteration
            self.rsi_status = is_overbought(curr_rsi) or is_oversold(curr_rsi)
            rsi_i += 1
            
        self.actions = actions
    
    
def pull_gains_and_losses(candle_list):
    gains = list()
    losses = list()
    
    for c in candle_list:
        gains.append(c.get_gain())
        losses.append(c.get_loss())
        
    return (gains,losses)

def index_of_time(data_list, curr_time):
    if isinstance(data_list, CandleList):
        candles = data_list.get_candle_list()
        time_list = [x.get_start_time() for x in candles]
    else:
        time_list = [x[0] for x in data_list]
        
    return time_list.index(curr_time)

def is_overbought(rsi):
    if rsi >= 70:
        return Trader.OVERBOUGHT

def is_oversold(rsi):
    if rsi <= 30:
        return Trader.OVERSOLD