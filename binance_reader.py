import dateparser
import pytz
from datetime import datetime
from binance import client
import config, csv


def date_to_milliseconds(str):
    # get epoch value in UTC
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # parse our date string
    d = dateparser.parse(str)
    # return the difference in time
    return int((d - epoch).total_seconds() * 1000.0)


c = client.Client()
if __name__ == '__main__':
    start_time = date_to_milliseconds(config.start_time_str)
    end_time = date_to_milliseconds(config.end_time_str)
    klines = c.get_klines(
        symbol='BTCUSDT',
        interval='15m',
        # limit=100,
        startTime=start_time,
        endTime=end_time
    )
    print(klines)

    csvfile = open('{}_to_{}_15minutes.csv'.format(config.start_time_str, config.end_time_str), 'w', newline='')
    kline_writer = csv.writer(csvfile, delimiter=',')

    for kline in klines:
        close_price = kline[4]
        print(close_price)
        kline_writer.writerow([close_price])

    csvfile.close()

# [
#     [
#         1499040000000,  # Open time
#         "0.01634790",  # Open
#         "0.80000000",  # High
#         "0.01575800",  # Low
#         "0.01577100",  # Close
#         "148976.11427815",  # Volume
#         1499644799999,  # Close time
#         "2434.19055334",  # Quote asset volume
#         308,  # Number of trades
#         "1756.87402397",  # Taker buy base asset volume
#         "28.46694368",  # Taker buy quote asset volume
#         "17928899.62484339"  # Can be ignored
#     ]
# ]
