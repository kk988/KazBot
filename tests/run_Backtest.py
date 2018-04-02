from lib.Backtest import Backtest

#btest1 = Backtest("2017-02-01", "2018-03-31", 3600, "StochRSI", 1, n_period=15)
#btest2 = Backtest("2018-01-01", "2018-03-31", 900, "MACD", 1)
#btest3 = Backtest("2017-02-01", "2018-03-31", 3600, "MACD", 1)
btest4 = Backtest("2017-12-31", "2018-03-31", 300, ["StochRSI", "MACD"], 1, n_period=15)
#btest5 = Backtest("2017-02-01", "2018-03-31", 21600, "MACD", 1)
#btest6 = Backtest("2017-02-01", "2018-03-31", 3600, "MACD", 1)
#btest7 = Backtest("2017-02-01", "2018-03-31", 900, "MACD", 1)

#btest1.generate_result_summary()
#btest2.generate_result_summary()
#btest3.generate_result_summary()
btest4.generate_result_summary()
#btest5.generate_result_summary()
#btest6.generate_result_summary()
#btest7.generate_result_summary()