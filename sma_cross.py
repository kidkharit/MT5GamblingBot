import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
import time






bars = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1,1,10)
bars_df = pd.DataFrame(bars)
# print(bars_df)

"""
- bot that trades with different strategies, uses different currency pairs (w/ low corr)
- save trade history to file
- (optional) can switch modes
    - changes parameters
    - changes strats
    
    1. make a simple bot that trade base on a simple condition
    1. check the official documentations to cover errors
        a. connection
    2. implement backtesting
    3. other functions
        a. send line notification
        b. machine learning

"""


if __name__ == '__main__':
    if mt5.initialize():
        print("heiwfew")

    
    
