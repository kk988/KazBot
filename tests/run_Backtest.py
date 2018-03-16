from lib.Backtest import Backtest

btest1 = Backtest("2018-1-1", "2018-2-1", 300, "StochRSI", 1, n_period=14)
btest2 = Backtest("2017-10-1", "2018-2-1", 900, "StochRSI", 1, n_period=14)

btest1.generate_result_summary()
btest2.generate_result_summary()