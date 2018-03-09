from Strategies.TradeAction import TradeAction

test_trades = [
    [1, TradeAction.BUY],
    [2, TradeAction.SELL],
    [3, TradeAction.HOLD]
    ]

trades = []

for trade in test_trades:
    trades.append(TradeAction(trade[0], trade[1]))
    
for action in trades:
    print action