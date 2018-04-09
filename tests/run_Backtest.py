from lib.Backtest import Backtest

#btest1 = Backtest("gdax", "2018-1-1", "2018-2-1", 900, "StochRSI", 1, n_period=15) #going down

btest2 = Backtest("poloniex", "2017-10-15", "2018-3-1", 900, "StochRSI", 1, n_period=15) #5mo, large increase from 10-12, fall from 12-1 
btest3 = Backtest("gdax", "2017-12-20", "2018-2-1", 900, "StochRSI", 1, n_period=15) #5mo, large increase from 10-12, fall from 12-1 
btest4 = Backtest("poloniex", "2018-01-01", "2018-4-6", 900, "StochRSI", 1, n_period=15) #5mo, large increase from 10-12, fall from 12-1 

#btest1.generate_result_summary()
btest2.generate_result_summary()
btest3.generate_result_summary()
btest4.generate_result_summary()