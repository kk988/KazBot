from Strategies.StochRSI import StochRSI
from exchanges.gdax import CandleList
from Strategies.Trader import Trader
from lib.Backtest import pull_candles
from datetime import datetime
from Strategies.TradeAction import TradeAction

test_input = [
    [1514764800, 225, 227.98, 227.18, 226.2, 2146.597926890001],
    [1514765700, 223.18, 225.94, 225.94, 224.51, 1731.3826289500005],
    [1514766600, 223.33, 225.34, 224.5, 224.25, 1183.6441438499999],
    [1514767500, 223.17, 225.21, 224.24, 223.86, 1725.7515062799991],
    [1514768400, 222.34, 224.49, 223.71, 222.4, 1408.105845859999],
    [1514769300, 222.38, 223.89, 222.4, 223.32, 2350.3959640400003],
    [1514770200, 220, 223.33, 223.33, 220, 2401.4318011600008],
    [1514771100, 217.66, 220.01, 220, 218.3, 3248.8890611900015],
    [1514772000, 218, 220.7, 218, 220.69, 2221.17999213],
    [1514772900, 218.51, 220.7, 220.69, 218.72, 1919.743389329999],
    [1514773800, 218, 218.85, 218.71, 218.85, 1570.0582422599996],
    [1514774700, 218.85, 220.98, 218.85, 219.18, 1273.239872649999],
    [1514775600, 219.17, 221.1, 219.17, 221.1, 1387.0172615699994],
    [1514776500, 221.09, 223, 221.09, 222.99, 2069.4196435700014],
    [1514777400, 221.5, 223.51, 223, 222.14, 1271.8401750599999],
    [1514778300, 220.35, 222.5, 222.13, 221.09, 1401.9549110199998],
    [1514779200, 220.1, 222.01, 221.09, 221, 853.6573286899999],
    [1514780100, 220.99, 225, 221, 225, 1724.5195501199998],
    [1514781000, 224.07, 225, 225, 224.76, 981.2409791199999],
    [1514781900, 224.01, 225.59, 224.75, 225.59, 1503.0952253800003],
    [1514782800, 223.67, 226.99, 225.6, 223.68, 1758.2038861200006],
    [1514783700, 222.51, 224.92, 223.67, 224, 1204.2934695400004],
    [1514784600, 223.66, 224.83, 224, 224.77, 620.2281478699996],
    [1514785500, 224.36, 224.77, 224.76, 224.36, 766.30519488],
    [1514786400, 224, 228.72, 224.37, 228.72, 1346.6303277200007],
    [1514787300, 227.22, 229.98, 228.69, 229.97, 1258.0223326400007],
    [1514788200, 229.38, 231, 229.98, 229.62, 1393.06231857],
    [1514789100, 229.62, 232.29, 229.62, 231.7, 1807.4421110799992],
    [1514790000, 229.16, 231.93, 231.7, 230.3, 1089.276233719999],
    [1514790900, 227.98, 230.3, 230.3, 228.33, 844.5188090500001],
    [1514791800, 227, 229.24, 227.81, 227.06, 707.40858715],
    [1514792700, 225.08, 227.1, 227, 226.08, 1034.3744035899997],
    [1514793600, 225.25, 227.5, 226.08, 227.48, 627.9822545099997],
    [1514794500, 226, 228.35, 227.48, 226.36, 1054.5007492999991],
    [1514795400, 223.73, 226.6, 226.24, 223.73, 901.6639771699997],
    [1514796300, 223.66, 227.49, 223.73, 225.3, 741.2675540499996],
    [1514797200, 225.29, 227.56, 225.29, 227.16, 683.7465314400004],
    [1514798100, 226.8, 227.89, 227.23, 227.42, 714.0197829199998],
    [1514799000, 226.79, 228.41, 227.41, 228.4, 517.1688123799997],
    [1514799900, 226.83, 229.12, 228.41, 228.61, 551.3185048799999],
    [1514800800, 226.53, 229.15, 228.61, 227.15, 471.8997491800005],
    [1514801700, 225.99, 228.09, 227.14, 228.09, 418.96999766999966],
    [1514802600, 227, 228.5, 228.08, 228.24, 670.5534044699997],
    [1514803500, 227.55, 228.15, 228.06, 228.15, 445.07435008999994],
    [1514804400, 222.62, 229.46, 228.15, 225.42, 905.0926133899997],
    [1514805300, 222.69, 225.42, 225.41, 223.15, 563.73308688],
    [1514806200, 223, 225.63, 223.24, 225.5, 350.98842097000005],
    [1514807100, 224.05, 226.25, 225, 226.21, 391.85412694],
    [1514808000, 226.2, 227.95, 226.21, 226.5, 939.8064556399999],
    [1514808900, 225.01, 226.51, 226.51, 225.25, 600.4237057000006],
    [1514809800, 225.25, 226.26, 225.25, 225.76, 352.84068472],
    [1514810700, 224.6, 225.76, 225.76, 224.6, 496.88434499],
    [1514811600, 222.54, 224.53, 223.68, 223.01, 749.5572771600001],
    [1514812500, 222.69, 224.46, 223, 222.69, 672.6920077700001],
    [1514813400, 222.64, 223.06, 222.69, 223.06, 495.03980977999987],
    [1514814300, 222.38, 223.22, 223.22, 222.43, 949.1309957200002],
    [1514815200, 221, 222.43, 222.42, 221.01, 1562.0329459900004],
    [1514816100, 220.4, 221.29, 221, 221.29, 1016.6143355400005],
    [1514817000, 220.6, 221.67, 221.28, 221.67, 896.9821059800003],
    [1514817900, 221.65, 225.22, 221.65, 225.22, 2327.8136566300022],
    [1514818800, 224.12, 225.5, 225.19, 225.12, 778.4755240499999],
    [1514819700, 224, 225.73, 225.11, 225.71, 887.27878068],
    [1514820600, 225, 225.79, 225.72, 225.04, 767.8186259000003],
    [1514821500, 225, 225.77, 225.04, 225.22, 866.0745182299999],
    [1514822400, 223.72, 225.22, 225.21, 224.45, 964.7040334499994],
    [1514823300, 222.06, 224.46, 224.46, 222.75, 1088.8602741500006],
    [1514824200, 222.12, 223.48, 222.88, 223.12, 1087.35424975],
    [1514825100, 222.37, 223.7, 223.12, 222.38, 784.7685125400002],
    [1514826000, 222.37, 223.14, 222.38, 222.81, 749.6849277800003],
    [1514826900, 222.68, 223.7, 222.81, 223.62, 821.4077913799998],
    [1514827800, 222.8, 223.8, 223.61, 223.13, 599.4085023800002],
    [1514828700, 222.4, 223.14, 223.14, 222.4, 788.9949952300002],
    [1514829600, 222.05, 222.77, 222.41, 222.05, 1998.6326394100001],
    [1514830500, 222, 223.9, 222.05, 223.01, 728.4527652700001],
    [1514831400, 222.67, 223.73, 223.01, 223.43, 743.1016400100001],
    [1514832300, 222.33, 223.43, 223.43, 222.5, 758.4159689100001],
    [1514833200, 222.2, 222.84, 222.49, 222.51, 825.1236259300005],
    [1514834100, 222.05, 222.8, 222.5, 222.5, 916.8006722099997],
    [1514835000, 221.15, 223.05, 222.51, 223.05, 1556.5997108900008],
    [1514835900, 222.11, 223.68, 223.29, 223.35, 1293.9438520200001],
    [1514836800, 222.65, 224.41, 223.35, 224.41, 1617.8976836900003],
    [1514837700, 223.49, 224.45, 224.4, 224.19, 1054.9859025399999],
    [1514838600, 224.2, 224.95, 224.2, 224.94, 1136.0685569700004],
    [1514839500, 224.12, 224.95, 224.94, 224.65, 1010.37963151],
    [1514840400, 224.2, 227.93, 224.65, 227.21, 4686.59493517],
    [1514841300, 226.51, 230, 227.21, 230, 2100.4598443899995],
    [1514842200, 228.8, 230.84, 230, 229.42, 2317.954855660001],
    [1514843100, 227.13, 229.43, 229.42, 227.89, 1725.3138771599993],
    [1514844000, 227.5, 228.35, 227.9, 228.35, 819.0218088599999],
    [1514844900, 228.06, 229.33, 228.35, 228.72, 1084.3019127400003]
]

HOLD = TradeAction.HOLD
BUY = TradeAction.BUY
SELL = TradeAction.SELL

expected_results =[
    [1514764800,HOLD],
    [1514765700,HOLD],
    [1514766600,SELL],
    [1514767500,HOLD],
    [1514768400,HOLD],
    [1514769300,HOLD],
    [1514770200,HOLD],
    [1514771100,HOLD],
    [1514772000,HOLD],
    [1514772900,HOLD],
    [1514773800,HOLD],
    [1514774700,HOLD],
    [1514775600,HOLD],
    [1514776500,HOLD],
    [1514777400,HOLD],
    [1514778300,HOLD],
    [1514779200,HOLD],
    [1514780100,HOLD],
    [1514781000,HOLD],
    [1514781900,HOLD],
    [1514782800,HOLD],
    [1514783700,HOLD],
    [1514784600,HOLD],
    [1514785500,HOLD],
    [1514786400,HOLD],
    [1514787300,HOLD],
    [1514788200,HOLD],
    [1514789100,HOLD],
    [1514790000,HOLD],
    [1514790900,HOLD],
    [1514791800,HOLD],
    [1514792700,BUY],
    [1514793600,HOLD],
    [1514794500,HOLD],
    [1514795400,HOLD],
    [1514796300,SELL],
    [1514797200,HOLD],
    [1514798100,HOLD],
    [1514799000,HOLD],
    [1514799900,HOLD],
    [1514800800,HOLD],
    [1514801700,HOLD],
    [1514802600,HOLD],
    [1514803500,HOLD],
    [1514804400,HOLD],
    [1514805300,HOLD],
    [1514806200,HOLD],
    [1514807100,HOLD],
    [1514808000,HOLD],
    [1514808900,HOLD],
    [1514809800,HOLD],
    [1514810700,HOLD],
    [1514811600,HOLD],
    [1514812500,HOLD],
    [1514813400,SELL],
    [1514814300,HOLD],
    [1514815200,HOLD],
    [1514816100,SELL],
    [1514817000,HOLD],
    [1514817900,HOLD],
    [1514818800,SELL],
    [1514819700,HOLD],
    [1514820600,HOLD],
    [1514821500,HOLD]
]

stoch_rsi_output = [
    [1514764800,0.95249858],
    [1514765700,1.00000000],
    [1514766600,0.83375205],
    [1514767500,0.62320001],
    [1514768400,0.33313260],
    [1514769300,0.19984739],
    [1514770200,0.39364354],
    [1514771100,0.22628271],
    [1514772000,0.00000000],
    [1514772900,0.20741616],
    [1514773800,0.43006203],
    [1514774700,0.45197065],
    [1514775600,0.56726096],
    [1514776500,0.59074968],
    [1514777400,0.37306394],
    [1514778300,0.63759278],
    [1514779200,0.87486166],
    [1514780100,0.89593195],
    [1514781000,0.18878677],
    [1514781900,0.00000000],
    [1514782800,0.44269674],
    [1514783700,0.65310927],
    [1514784600,0.70309999],
    [1514785500,0.47383388],
    [1514786400,0.57109910],
    [1514787300,0.35892345],
    [1514788200,0.24099474],
    [1514789100,0.20228224],
    [1514790000,0.29837328],
    [1514790900,0.13249291],
    [1514791800,0.00000000],
    [1514792700,0.09482196],
    [1514793600,0.22545310],
    [1514794500,1.00000000],
    [1514795400,0.98414807],
    [1514796300,1.00000000],
    [1514797200,0.84765864],
    [1514798100,0.88332287],
    [1514799000,0.70648080],
    [1514799900,0.35220604],
    [1514800800,0.40943154],
    [1514801700,0.26173366],
    [1514802600,0.37312200],
    [1514803500,0.57706352],
    [1514804400,0.42547342],
    [1514805300,0.15813175],
    [1514806200,0.00000000],
    [1514807100,0.35057547],
    [1514808000,0.49630020],
    [1514808900,0.23510363],
    [1514809800,0.24411450],
    [1514810700,0.33344452],
    [1514811600,0.87302506],
    [1514812500,0.92406130],
    [1514813400,1.00000000],
    [1514814300,0.89386563],
    [1514815200,1.00000000],
    [1514816100,0.86971156],
    [1514817000,1.00000000],
    [1514817900,1.00000000],
    [1514818800,0.87803328],
    [1514819700,0.58681788],
    [1514820600,0.63543200],
    [1514821500,0.67444251]
]

expected_output = []

for action in expected_results:
    expected_output.append(TradeAction(action[0], action[1]))

def trade_action_is_equal(t_a1, t_a2):
    return t_a1.get_time() == t_a2.get_time() and t_a1.get_action() == t_a2.get_action()

my_trader = Trader(stoch_rsi_output)

my_vals = my_trader.get_actions()

print "My Output          Correct Output"
for pair in zip(my_vals,expected_output):
    print str(pair[0]) + "   " + str(pair[1])

correct_output = len(my_vals) == len(expected_output)

while correct_output and my_vals:
    curr_val = my_vals.pop(0)
    curr_expect = expected_output.pop(0)
    
    if not trade_action_is_equal(curr_val, curr_expect):
        correct_output = False

if correct_output:
    print "Correct Output"
else:
    print "There's a problem"
