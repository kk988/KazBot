class TradeAction():
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    
    def __init__(self, time, action):
        self.time = time
        self.action = action
        self.tpl = (time, action)
    
    def __str__(self):
        return str(self.time) + ": " + self.action
    
    def __eq__(self, other):
        return self.tpl == other.tpl
    
    def __hash__(self):
        return hash(self.tpl)
    
    def get_time(self):
        return self.time
    
    def get_action(self):
        return self.action