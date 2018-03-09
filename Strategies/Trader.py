from TradeAction import TradeAction

class Trader():
    HIGH = "HIGH"
    LOW = "LOW"
    s_rsi_high_thresh = 0.8
    s_rsi_low_thresh = 0.2
    PERSISTANCE_LIMIT = 3
    
    def __init__(self, data):
        self.data = data
        self.persisted = False
        self.persistance = 0
        self.trend = None
        self.run_actions()
    
    #returns a list of TradeActions
    def get_actions(self):
        return self.actions
    
    #Trade Actions = [time, action, shares=0]
    def run_actions(self):
        actions = []
        
        for candle in self.data:
            #test if above high thresh
            if candle[1] >= self.s_rsi_high_thresh:
                #test if already in high trend
                if self.trend == self.HIGH:
                    #increase persistence
                    self.persistance += 1
                #not already in trend, start trend, reset persistance
                else:
                    self.trend = self.HIGH
                    self.persistance = 0
            
            #test if below low thresh
            elif candle[1] <= self.s_rsi_low_thresh:
                #test if already in low trend
                if self.trend == self.LOW:
                    #increase persistance
                    self.persistance += 1
                #not already in trend, start trend reset persistance
                else:
                    self.trend = self.LOW
                    self.persistance = 0
            #not in trend. so end the trend
            elif self.trend:
                self.trend = None
                
            #test if persisted
            if self.persistance == self.PERSISTANCE_LIMIT:
                self.persistance = 0
                self.persisted = True
                
            #generate TradeAction
            if self.persisted:
                self.persisted = False
                
                if self.trend == self.HIGH:
                    action = TradeAction.SELL
                    shares = "all"
                else:
                    action = TradeAction.BUY
                    shares = "all"
            else:
                action = TradeAction.HOLD
                shares = 0
            
            actions.append(TradeAction(candle[0], action, shares))
                    
        self.actions = actions











#buy if the previous stoch rsi was 1 and the current is not,
#sell if the previous stoch rsi was 0 and the current is not
#def stoke_limit_change(s_rsi, prev_s_rsi):
#    if (s_rsi != 1 and prev_s_rsi == 1):
#        return "SELL"
#    elif (s_rsi != 0 and prev_s_rsi == 0):
#        return "BUY"
#    else:
#        return "HOLD"

#buy if the rsi/stoch rsi is above high thresh
#sell if it's below low thresh
#def thresh_test(high, low, rsi):
#    if rsi >= high:
#        return "BUY"
#    elif rsi <= low:
#        return "SELL"
#    else:
#        return "HOLD"