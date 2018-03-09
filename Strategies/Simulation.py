from TradeAction import TradeAction
from exchanges.gdax import CandleList
from exchanges.gdax import Candle

def get_curr_price(candle):
    return candle.get_close_price()
    
def convert_trade_actions_to_dict(trade_actions):
    actions_dict = dict()
    for action in trade_actions:
        actions_dict[action.get_time()] = action.get_action()
        
    return actions_dict

class Simulation():
    SHARE_TRADE_RATIO = 1.0
    
    def __init__(self, candle_list, trade_actions, account_balance, starting_shares=0):
        self.candles = candle_list.get_candle_list()
        self.trade_actions = convert_trade_actions_to_dict(trade_actions)
        self.shares = starting_shares
        self.account = account_balance
        self.end_value = None
        self.value_change = None
        self.value_percent_change = None
        self.start_price = self.candles[0].get_open_price()
        self.end_price = self.candles[-1].get_close_price()
        self.price = self.start_price
        self.start_value = self.value()
        self.price_change = self.end_price - self.start_price
        self.price_change_percent = self.price_change / self.start_price
        self.trades = 0
        self.run()
        
    def get_shares(self):
        return self.shares
    
    def get_account_balance(self):
        return self.account
    
    def get_start_value(self):
        return self.start_value
    
    def get_end_value(self):
        return self.end_value
    
    def get_value_change(self):
        return self.value_change
    
    def get_value_change_percent(self):
        return self.value_percent_change
    
    def get_price_change(self):
        return self.price_change
    
    def get_price_change_percent(self):
        return self.price_change_percent
    
    def get_start_price(self):
        return self.start_price
    
    def get_end_price(self):
        return self.end_price
    
    def get_trades(self):
        return self.trades
    
    def value(self):
        return self.shares * self.price + self.account
    
    def run(self):
        for candle in self.candles:
            self.execute_action(candle)
            
        self.end_value = self.value()
        self.value_change = self.end_value - self.start_value
        self.value_percent_change = self.value_change / self.start_value
    
    def execute_action(self, candle):
        time = candle.get_start_time()
        
        action = None
        
        if time in self.trade_actions.keys():
            action = self.trade_actions[time]
        
        #print "account: ", self.account
        #print "shares: ", self.shares
        #print "price: ", candle.get_close_price()
        
        if action == TradeAction.HOLD:
            return
        if action == TradeAction.BUY:
            if self.account == 0:
                return               
            curr_price = get_curr_price(candle)
            self.shares += (self.account * self.SHARE_TRADE_RATIO) / curr_price
            self.account *= (1 - self.SHARE_TRADE_RATIO)
            self.trades += 1
            return
        if action == TradeAction.SELL:
            if self.shares == 0:
                return
            
            curr_price = get_curr_price(candle)
            self.account += curr_price * self.shares * self.SHARE_TRADE_RATIO
            self.shares *= (1 - self.SHARE_TRADE_RATIO)
            self.trades += 1
            return
        
        return
        
    
    