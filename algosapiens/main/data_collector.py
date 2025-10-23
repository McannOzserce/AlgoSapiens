import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from datacollection.data_collection import fetch_binance_data as mainfunction

mainfunction(50000, 'BTCUSDT')

# 1. parameter determines how many candles will be drawn.
# 2. parameter determines which coin's candles will be drawn.