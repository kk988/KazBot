'''
Created on Feb 11, 2018

@author: kristakazmierkiewicz
'''
from StochRSI import StochRSI
from Trader import Trader
import RSI

def run_strategy(strategy, data, **kwargs):
    if strategy == 'StochRSI':
        if 'n_period' in kwargs:
            return Trader(StochRSI(data, kwargs['n_period']).get_stoch_rsi_vals()).get_actions()
        else:
            raise RuntimeError("StochRSI Strategy requires a specific n_period.")
        
    if strategy == "RSI_Rollercoaster":
        if 'swing_period' in kwargs and 'n_period' in kwargs:
            return RSI.Trader(data, RSI.RSI(data, kwargs['n_period']), kwargs['swing_period'])