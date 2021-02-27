from binance import client
import config, csv


def get_klines(symbol, interval):
    return c.get_historical_klines(
        symbol=symbol,
        interval=interval,
        start_str=config.start_time_str,
        end_str=config.end_time_str
    )

def write_closing_prices_to_csv(symbol, kline_array):
    csvfile = open('{}_close_{}_to_{}_{}.csv'.format(symbol, config.start_time_str, config.end_time_str, config.candlestick_interval), 'w', newline='')
    kline_writer = csv.writer(csvfile, delimiter=',')

    for kline in kline_array:
        close_price = kline[4]
        print(close_price)
        kline_writer.writerow([close_price])

    csvfile.close()

c = client.Client()
if __name__ == '__main__':
    for symbol in config.symbols:
        klines = get_klines(symbol, config.candlestick_interval)
        write_closing_prices_to_csv(symbol, klines)