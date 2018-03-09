class TradeAction():
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    
    def __init__(self, time, action):
        self.time = time
        self.action = action
    
    def __str__(self):
        return str(self.time) + ": " + self.action
    
    def get_time(self):
        return self.time
    
    def get_action(self):
        return self.action