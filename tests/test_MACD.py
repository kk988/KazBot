from Strategies.MACD import MACD

test_input = [
    [1,    459.99],
    [2,    448.85],
    [3,    446.06],
    [4,    450.81],
    [5,    442.8],
    [6,    448.97],
    [7,    444.57],
    [8,    441.4],
    [9,    430.47],
    [10,    420.05],
    [11,    431.14],
    [12,    425.66],
    [13,    430.58],
    [14,    431.72],
    [15,    437.87],
    [16,    428.43],
    [17,    428.35],
    [18,    432.5],
    [19,    443.66],
    [20,    455.72],
    [21,    454.49],
    [22,    452.08],
    [23,    452.73],
    [24,    461.91],
    [25,    463.58],
    [26,    461.14],
    [27,    452.08],
    [28,    442.66],
    [29,    428.91],
    [30,    429.79],
    [31,    431.99],
    [32,    427.72],
    [33,    423.2],
    [34,    426.21],
    [35,    426.98],
    [36,    435.69],
    [37,    434.33],
    [38,    429.8],
    [39,    419.85],
    [40,    426.24],
    [41,    402.8],
    [42,    392.05],
    [43,    390.53],
    [44,    398.67],
    [45,    406.13],
    [46,    405.46],
    [47,    408.38],
    [48,    417.2],
    [49,    430.12],
    [50,    442.78],
    [51,    439.29],
    [52,    445.52],
    [53,    449.98],
    [54,    460.71],
    [55,    458.66],
    [56,    463.84],
    [57,    456.77],
    [58,    452.97],
    [59,    454.74],
    [60,    443.86],
    [61,    428.85],
    [62,    434.58],
    [63,    433.26],
    [64,    442.93],
    [65,    439.66],
    [66,    441.35]]

expected_out = {
    34:    -5.10808405883,
    35:    -4.52749455759,
    36:    -3.38777517583,
    37:    -2.59227244014,
    38:    -2.25061327857,
    39:    -2.55208694964,
    40:    -2.19226272349,
    41:    -3.33549666884,
    42:    -4.54343971902,
    43:    -5.12922635656,
    44:    -4.66618032746,
    45:    -3.60278078271,
    46:    -2.72946258713,
    47:    -1.78573807116,
    48:    -0.46676156132,
    49:    1.28098896595,
    50:    3.1863545444,
    51:    4.05271015411,
    52:    4.83348939785,
    53:    5.39572753013,
    54:    6.1793536733,
    55:    6.23098881483,
    56:    6.2683194036,
    57:    5.49867409504,
    58:    4.45972917676,
    59:    3.65175545226,
    60:    2.21528877848,
    61:    0.1915808139,
    62:    -0.77097080332,
    63:    -1.46610896521,
    64:    -1.25249957861,
    65:    -1.3034484609,
    66:    -1.19804008095}

macd = MACD(test_input)

histo = macd.get_histogram()

histo = {k: round(v, 11) for (k, v) in histo.items()}

print(histo)

if len(histo) == len(expected_out):
    for time in sorted(histo.keys()):
        if not histo[time] == expected_out[time]:
            print(time, ": ")
            print(histo[time], expected_out[time])
else:
    print("Different number of results")

print(histo == expected_out)