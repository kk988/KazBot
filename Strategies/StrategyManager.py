'''
Created on Feb 11, 2018

@author: kristakazmierkiewicz
'''
from StochRSI import StochRSI
from Trader import Trader
import MACD

def run_strategy(strategy, data, **kwargs):
    if isinstance(strategy, str):
        strategy = [strategy]
    
    trades = set()
    
    if 'StochRSI' in strategy:
        if 'n_period' in kwargs:
            trades = set(Trader(StochRSI(data, kwargs['n_period']).get_stoch_rsi_vals()).get_actions())
        else:
            raise RuntimeError("StochRSI Strategy requires a specific n_period.")
    
    if 'MACD' in strategy:
        if trades:
            trades = trades & set(MACD.Trader(data).get_actions())
            
    return list(trades)