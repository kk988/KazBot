from Strategies.TradeAction import TradeAction

test_trades = [
    [1, TradeAction.BUY, 20],
    [2, TradeAction.SELL, 50],
    [3, TradeAction.HOLD, 0]
    ]

trades = []

for trade in test_trades:
    trades.append(TradeAction(trade[0], trade[1], trade[2]))
    
for action in trades:
    print action