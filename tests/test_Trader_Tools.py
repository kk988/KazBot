from Strategies.TraderTools import *
from exchanges.gdax import CandleList

test_input = [
    {'date': 1, 'low': 1, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 4, avg 4 
    {'date': 2, 'low': 2, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 3, avg 3.5
    {'date': 3, 'low': 3, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 2, avg 3
    {'date': 4, 'low': 1, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 4, avg 3
    {'date': 5, 'low': 2, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 3, avg 3
    {'date': 6, 'low': 3, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 2, ...
    {'date': 7, 'low': 1, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 4
    {'date': 8, 'low': 2, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 3
    {'date': 9, 'low': 3, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 2
    {'date': 10, 'low': 1, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 4 
    {'date': 11, 'low': 2, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 3
    {'date': 12, 'low': 3, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 2
    {'date': 13, 'low': 1, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 }, #len 4
    {'date': 14, 'low': 2, 'high': 5, 'open': 2, 'close': 4, 'volume': 1 } #len 3
    ]

cl = CandleList(test_input)

expected = [4.0, 3.5]

last_12 = [3.0 for _ in range(12)]

expected += last_12

print("Expected:", expected)

out = [average_candle_length(cl, n, 3) for n in range(1, 15)]

print("Out:", out)

if expected == out:
    print("SUCCESS!")
else:
    print("Failure of the worst kind...")