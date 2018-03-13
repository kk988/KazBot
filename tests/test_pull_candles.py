from lib.Backtest import pull_candles
import datetime
import math

granularity = 900
start = datetime.datetime(2018, 1, 1, 0, 0, 0)
end = datetime.datetime(2018, 1, 31, 0, 0, 0)
time_delta = end - start
expected_num_of_candles = int(math.ceil(time_delta.total_seconds() / granularity))

test_input=pull_candles( start, end, granularity )

for candle in test_input:
    print candle

print "\n\nExpected Candles:", expected_num_of_candles
print "Actual Candles: ", len(test_input)

print "\n"
first_candle_time = test_input[0][0]
last_candle_time = test_input[-1][0]

first_candle_time = datetime.datetime.fromtimestamp(first_candle_time)
last_candle_time = datetime.datetime.fromtimestamp(last_candle_time)

print "First candle time:", first_candle_time
print "Last candle time:", last_candle_time


if len(test_input) == expected_num_of_candles:
    print "\nSUCCESS!!!"
else:
    print "\nFailure!!!"