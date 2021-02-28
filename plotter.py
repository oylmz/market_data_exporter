import pandas as pd
import matplotlib.pyplot as plt
import config, util


def get_data_frames():
    df_list = []
    for symbol in config.symbols:
        filename = util.make_filename_for_symbol(symbol, config.start_time_str, config.end_time_str, config.candlestick_interval)
        df_list.append(pd.read_csv(filename, index_col=None, header=0))
    return df_list


if __name__ == '__main__':
    df_merged = pd.concat(get_data_frames(), axis=1, ignore_index=True)

    fig, ax1 = plt.subplots()
    fig.set_size_inches(15, 8, forward=True)
    ax1.set_xlabel('time (candle ticks)')
    ax1.set_ylabel(config.symbols[0], color=config.colors[0])
    ax1.plot(df_merged[0], color=config.colors[0])
    ax1.tick_params(axis='y', labelcolor=config.colors[0])

    for i in range(1, len(config.symbols)):
        ax_new = ax1.twinx()
        ax_new.set_ylabel(config.symbols[i], color=config.colors[i], labelpad=25 * i)
        ax_new.plot(df_merged[i], color=config.colors[i])
        ax_new.tick_params(axis='y', labelcolor=config.colors[i])

    fig.tight_layout()
    plt.show()
