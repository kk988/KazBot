from Strategies.EMA import EMA
from collections import Counter

test_data = [
    [1,22.27],
    [2,22.19],
    [3,22.08],
    [4,22.17],
    [5,22.18],
    [6,22.13],
    [7,22.23],
    [8,22.43],
    [9,22.24],
    [10,22.29],
    [11,22.15],
    [12,22.39],
    [13,22.38],
    [14,22.61],
    [15,23.36],
    [16,24.05],
    [17,23.75],
    [18,23.83],
    [19,23.95],
    [20,23.63],
    [21,23.82],
    [22,23.87],
    [23,23.65],
    [24,23.19],
    [25,23.10],
    [26,23.33],
    [27,22.68],
    [28,23.10],
    [29,22.40],
    [30,22.17]]

expected_ema = [
    22.22,
    22.21,
    22.24,
    22.27,
    22.33,
    22.52,
    22.80,
    22.97,
    23.13,
    23.28,
    23.34,
    23.43,
    23.51,
    23.53,
    23.47,
    23.40,
    23.39,
    23.26,
    23.23,
    23.08,
    22.92]

ema_results = EMA(test_data, 10).get_results()
emas = [round(x[1], 2) for x in ema_results]

if len(emas) == len(expected_ema):
    for i in range(len(emas)):
        print emas[i], expected_ema[i]
else:
    print "Differing number of values"

collect_results = Counter(emas)
collect_expect = Counter(expected_ema)

if emas == expected_ema:
    print "SUCCESS!!"
else:
    print "There was a problem."
    print collect_expect - collect_results