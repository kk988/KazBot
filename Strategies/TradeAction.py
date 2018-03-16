class TradeAction():
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    
    def __init__(self, time, action, trade_percent = 1.0):
        self.time = time
        self.action = action
        self.trade_percent = trade_percent
    
    def __str__(self):
        return str(self.time) + ": " + self.action
    
    def get_trade_percent(self):
        return self.trade_percent
    
    def get_time(self):
        return self.time
    
    def get_action(self):
        return self.action