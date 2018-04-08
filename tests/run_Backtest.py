from lib.Backtest import Backtest

#btest1 = Backtest("2018-1-1", "2018-2-1", 900, "StochRSI", 1, n_period=15) #going down

btest2 = Backtest("2017-10-15", "2018-3-1", 900, "StochRSI", 1, n_period=15) #5mo, large increase from 10-12, fall from 12-1 

#btest1.generate_result_summary()
btest2.generate_result_summary()