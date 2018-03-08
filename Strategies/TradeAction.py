class TradeAction():
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    
    def __init__(self, time, action, shares=0):
        self.time = time
        self.action = action
        self.shares = shares
    
    def __str__(self):
        ret_str = str(self.time) + ": " + self.action
        
        if self.action != self.HOLD:
            ret_str += " " + str(self.shares) + " shares"
        
        return ret_str
    
    def get_time(self):
        return self.time
    
    def get_action(self):
        return self.action
    
    def get_shares(self):
        return self.shares
    
    #@classmethod
    #def BUY(cls):
    #    return "BUY"
        
    #@classmethod
    #def SELL(cls):
    #    return "SELL"
   # 
   # @classmethod
   # def HOLD(cls):
   #     return "HOLD"