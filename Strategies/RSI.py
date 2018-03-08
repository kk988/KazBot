from exchanges.gdax import CandleList

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
        
    
def pull_gains_and_losses(candle_list):
    gains = list()
    losses = list()
    
    for c in candle_list:
        gains.append(c.get_gain())
        losses.append(c.get_loss())
        
    return (gains,losses)