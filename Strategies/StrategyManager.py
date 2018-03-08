'''
Created on Feb 11, 2018

@author: kristakazmierkiewicz
'''
from StochRSI import StochRSI

def run_strategy(strategy, data, **kwargs):
    if strategy == 'StochRSI':
        return StochRSI(data, **kwargs)