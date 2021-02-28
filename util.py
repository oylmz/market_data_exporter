def make_filename_for_symbol(symbol, start_time, end_time, candlestick_interval):
    return '{}_close_{}_to_{}_{}.csv'.format(symbol, start_time, end_time, candlestick_interval)
