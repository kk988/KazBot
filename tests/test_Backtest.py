from lib.Backtest import Backtest

b_test1 = Backtest("2016-2-1", "2018-2-1", 86400, "RSI_Rollercoaster", 1, n_period=14, swing_period=7)

b_test1.generate_result_summary()