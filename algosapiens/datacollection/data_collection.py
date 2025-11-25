# AlgoSapiens - Data Collection Script
# Fetches historical kline (candle) data from the Binance API.
# This script retrieves data in batches and saves it as a Parquet file.

import pandas as pd
from binance.client import Client
from pathlib import Path
import time
import math

def fetch_binance_data(total_candles, symbol, interval=Client.KLINE_INTERVAL_5MINUTE):
    
    # 1. Initialize API Client
    try:
        client = Client()
        client.ping()
        print("Binance API connection successful.")
    except Exception as e:
        print(f"API connection error: {e}")
        return None

    # 2. Set Parameters
    limit_per_request = 1000  
    num_requests = math.ceil(total_candles / limit_per_request)
    
    all_klines_data = []
    endTime = None  

    print(f"Starting: Fetching {total_candles} {interval} candles for {symbol}...")
    print(f"Total of {num_requests} API requests will be made.")

    try:
        # 3. Data Fetching Loop
        for i in range(num_requests):
            klines = client.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit_per_request,
                endTime=endTime
            )
            all_klines_data = klines + all_klines_data
            endTime = klines[0][0]

            print(f"Request {i + 1}/{num_requests} completed. {len(all_klines_data)} candles fetched.")
            time.sleep(0.5) 

        print("All data fetched. Creating DataFrame...")

        # 4. Convert to Pandas DataFrame
        columns = [
            'open_time', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ]
        
        df = pd.DataFrame(all_klines_data, columns=columns)

        # 5. Clean and Transform Data
        
        # Select only the main columns we need for AlgoSapiens
        # IMPORTANT: We are taking 'quote_asset_volume' (USDT amount) instead of 'volume' (BTC amount).
        df = df[['open_time', 'open', 'high', 'low', 'close', 'quote_asset_volume']]
        
        # To keep future code simple, we rename 'quote_asset_volume' to 'volume'.
        # Our 'volume' column now represents the USDT (Dollar) volume.
        df = df.rename(columns={'quote_asset_volume': 'volume'})

        # Convert the timestamp (milliseconds) to a readable 'datetime' format
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        
        # Convert columns that should be numeric to float
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = pd.to_numeric(df[col])

        # Ensure the data is sorted from oldest to newest
        df = df.sort_values(by='open_time')
        
        # Ensure there are no duplicate candles
        df = df.drop_duplicates(subset='open_time')

        print(f"DataFrame created. Total {len(df)} unique candles.")
        
        # 6. Define File Path and Save
        script_dir = Path(__file__).resolve().parent
        data_dir = script_dir.parent / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)
        file_path = data_dir / f'data.parquet'
        
        # 7. Save as Parquet
        df.to_parquet(file_path, index=False, engine='pyarrow')
        
        print(f"Success! Data saved to: {file_path}")
        
        return df

    except Exception as e:
        print(f"An error occurred during data fetching or saving: {e}")
        return None