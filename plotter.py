import pandas as pd
import matplotlib.pyplot as plt
import config

if __name__ == '__main__':
    df_btc = pd.read_csv('BTCUSDT_close_01-01-2021_to_27-02-2021_15m.csv', index_col=None, header=0)
    df_eth = pd.read_csv('ETHUSDT_close_01-01-2021_to_27-02-2021_15m.csv', index_col=None, header=0)
    df_ltc = pd.read_csv('LTCUSDT_close_01-01-2021_to_27-02-2021_15m.csv', index_col=None, header=0)
    df_ada = pd.read_csv('ADAUSDT_close_01-01-2021_to_27-02-2021_15m.csv', index_col=None, header=0)
    df_dot = pd.read_csv('DOTUSDT_close_01-01-2021_to_27-02-2021_15m.csv', index_col=None, header=0)

    df_merged = pd.concat([df_btc, df_eth, df_ltc, df_ada, df_dot], axis=1, ignore_index=True)

    fig, ax1 = plt.subplots()
    fig.set_size_inches(15, 8, forward=True)
    color = 'tab:red'
    ax1.set_xlabel('time (candle ticks)')
    ax1.set_ylabel(config.symbols[0], color=color)
    ax1.plot(df_merged[0], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel(config.symbols[1], color=color)
    ax2.plot(df_merged[1], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx()
    color = 'tab:green'
    ax3.set_ylabel(config.symbols[2], color=color, labelpad=25)
    ax3.plot(df_merged[2], color=color)
    ax3.tick_params(axis='y', labelcolor=color)

    ax4 = ax1.twinx()
    color = '#0f0f0f'
    ax4.set_ylabel(config.symbols[3], color=color, labelpad=50)
    ax4.plot(df_merged[3], color=color)
    ax4.tick_params(axis='y', labelcolor=color)

    ax5 = ax1.twinx()
    color = '#9467bd'
    ax5.set_ylabel(config.symbols[4], color=color, labelpad=75)
    ax5.plot(df_merged[4], color=color)
    ax5.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()
