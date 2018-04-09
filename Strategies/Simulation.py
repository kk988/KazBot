from __future__ import print_function
from .TradeAction import TradeAction
from exchanges.gdax import CandleList
from exchanges.gdax import Candle
import datetime

def get_curr_price(candle):
    return candle.get_close_price()
    
def convert_trade_actions_to_dict(trade_actions):
    actions_dict = dict()
    for action in trade_actions:
        actions_dict[action.get_time()] = action.get_action()
        
    return actions_dict

class Simulation():
    #Share Trade Ratio
    #Percentage of your balance or shares that you are buying or selling
    #every time Trader determines a buy or sell action
    
    def __init__(self, candle_list, trade_actions, account, share_trade_ratio=1.0):
        self.candles = candle_list.get_candle_list()
        self.trade_actions = convert_trade_actions_to_dict(trade_actions)
        self.account = account
        self.end_value = None
        self.value_change = None
        self.value_percent_change = None
        self.start_price = self.candles[0].get_open_price()
        self.end_price = self.candles[-1].get_close_price()
        self.price = self.start_price
        self.start_datetime = datetime.datetime.fromtimestamp(self.candles[0].get_start_time())
        self.end_datetime = datetime.datetime.fromtimestamp(self.candles[-1].get_start_time())
        self.start_value = self.account.value(self.price)
        self.price_change = self.end_price - self.start_price
        self.price_change_percent = self.price_change / self.start_price
        self.share_trade_ratio = share_trade_ratio
        self.trades = 0
        self.run()
    
    def get_account(self):
        return self.account
    
    def get_start_datetime(self):
        return self.start_datetime
    
    def get_end_datetime(self):
        return self.end_datetime
    
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
    
    def run(self):
        for candle in self.candles:
            self.execute_action(candle)
            
        self.end_value = self.account.value(self.get_end_price())
        self.value_change = self.end_value - self.start_value
        self.value_percent_change = self.value_change / self.start_value
    
    def is_actionable(self, time):
        return time in self.trade_actions and not self.trade_actions[time] == TradeAction.HOLD
    
    def execute_action(self, candle):
        time = candle.get_start_time()
        
        if not self.is_actionable(time):
            return
        
        action = self.trade_actions[time]
        
        curr_price = get_curr_price(candle)
        
        if action == TradeAction.BUY:
            if self.account.get_balance() == 0:
                return               
            shares_to_buy = self.account.get_balance() * self.share_trade_ratio / curr_price
            self.account.buy(curr_price, shares_to_buy)
            print("[%s] Buy $%s" % (datetime.datetime.fromtimestamp(time), curr_price), end="\t")
            self.trades += 1
            return
        
        if action == TradeAction.SELL:
            if self.account.get_shares() == 0:
                return
            shares_to_sell = self.account.get_shares() * self.share_trade_ratio
            print("[%s] Sell $%s" % (datetime.datetime.fromtimestamp(time),curr_price), end="\t")
            self.account.sell(curr_price, shares_to_sell)
            self.trades += 1
            return
        
        raise AttributeError("Invalid Action: " + str(action))
        
        return
        
    
    