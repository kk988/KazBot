from TradeAction import TradeAction

class Trader():
    HIGH = "HIGH"
    LOW = "LOW"
    s_rsi_high_thresh = 0.8
    s_rsi_low_thresh = 0.2
    PERSISTENCE_LIMIT = 3
    
    def __init__(self, data):
        self.data = data
        self.persistence = 0
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
                self.set_trend_and_persistence(self.HIGH)
                    
            #test if below low thresh
            elif candle[1] <= self.s_rsi_low_thresh:
                self.set_trend_and_persistence(self.LOW)
                    
            #not in trend. so end the trend
            elif self.trend:
                self.trend = None
                self.persistence = 0
            
            actions.append(self.generate_trade_action(candle[0]))
             
        self.actions = actions     
    
    def set_trend_and_persistence(self, curr_trend):
        #test if already in curr trend
        if self.trend == curr_trend:
            #increase persistence
            self.persistence += 1
        #not already in trend, start trend
        else:
            self.trend = curr_trend
            self.persistence = 0
                  
    def generate_trade_action(self, candle_time):                    
        #if persisted
        if self.persistence == self.persistence_LIMIT:
            self.persistence = 0
                
            if self.trend == self.HIGH:
                return TradeAction(candle_time, TradeAction.SELL, 'all')
            else:
                return TradeAction(candle_time, TradeAction.BUY, 'all')
        return TradeAction(candle_time, TradeAction.HOLD, 'all')
                    
        
        










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