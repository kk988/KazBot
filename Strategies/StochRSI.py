import RSI

class StochRSI():
    def __init__(self, candles, n_period):
        self.n_period = n_period
        self.candles = candles
        rsi_obj = RSI.RSI(self.candles, n_period)
        self.rsi_list = rsi_obj.get_calculated_rsi_vals()
        self.vals = []
        self.run()
    
    def run(self):
        test_range = self.rsi_list[:self.n_period]
        
        curr_rsi_list = self.rsi_list[self.n_period:]
        
        for _ in range(len(curr_rsi_list) + 1):
            #calculate max rsi
            max_rsi = max([x[1] for x in test_range])
            
            #calculate min rsi
            min_rsi = min([x[1] for x in test_range])
            
            #current RSI is the last in the test range
            curr_rsi = test_range[-1]
            
            #calculate Stoch RSI
            s_rsi = ((curr_rsi[1] - min_rsi) / (max_rsi - min_rsi))
            
            #append rsi to current list of values
            self.vals.append([curr_rsi[0], s_rsi])
            
            #prep for next rsi
            if curr_rsi_list:
                test_range.pop(0)
                test_range.append(curr_rsi_list.pop(0))
    
    def get_stoch_rsi_vals(self):
        return self.vals
        
        #run stochRSI from this.
        #http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:stochrsi
        # n_period StochRSI = (RSI - Lowest Low RSI) / (Highest High RSI - Lowest Low RSI)