def average_candle_length(candle_list, time, period):
    candles = candle_list.get_candle_list()
    candle_lengths = {c.get_start_time(): float( c.get_high() - c.get_low() ) for c in candles}
    candle_times = sorted(candle_lengths.keys())
    current_i = candle_times.index(time)
    if not current_i - period + 1 < 0:
        start_i = current_i - period + 1
    else:
        start_i = 0
    
    period_of_interest = [ candle_lengths[x] for x in candle_times[start_i:current_i + 1] ]
    
    return sum(period_of_interest) / len(period_of_interest)

def swing_high(candle_list, time, period):
    close_prices = {candle.get_start_time(): candle.get_close_price() for candle in candle_list.get_candle_list()}
    times = sorted(close_prices.keys())
    swing_start = times.index(time)
    
    if swing_start < period:
        swing_range = times[:swing_start + 1]
    else:
        swing_range = times[swing_start - period + 1 : swing_start + 1]
    
    return max([close_prices[time] for time in swing_range])
    
def swing_low(candle_list, time, period):
    close_prices = {candle.get_start_time(): candle.get_close_price() for candle in candle_list.get_candle_list()}
    
    times = sorted(close_prices.keys())
    
    swing_start = times.index(time)
    
    if swing_start < period:
        swing_range = times[:swing_start + 1]
    else:
        swing_range = times[swing_start - period + 1 : swing_start + 1]
    
    return min([close_prices[time] for time in swing_range])
