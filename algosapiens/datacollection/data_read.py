# AlgoSapiens - Data Loading Utility
# Loads the Parquet data file from the /data directory into a pandas DataFrame.
# Also configures pandas display options for better readability.

import pandas as pd
from pathlib import Path

# --- Configuration ---
# Tell pandas not to use scientific notation (e.g., e+06).
# Format all floating-point numbers to 2 decimal places for printing.
pd.set_option('display.float_format', lambda x: '%.5f' % x)
# ---------------------

def load_data(file_name="btcusdt_5m_50000_islenmis.parquet"):
    """
    Reads the specified Parquet file from the root 'data' folder
    and returns it as a pandas DataFrame.
    
    This script assumes it is located within a subfolder 
    (like '/datacollection').
    """
    
    try:
        # 1. Define File Path
        # Get the full path of this script (e.g., .../AlgoSapiens/datacollection/data_read.py)
        script_path = Path(__file__).resolve()
        
        # Get the directory this script is in (e.g., .../AlgoSapiens/datacollection/)
        script_dir = script_path.parent
        
        # Get the parent directory (the project root) (e.g., .../AlgoSapiens/)
        project_root = script_dir.parent
        
        # Define the full path to the data file
        file_path = project_root / 'data' / file_name
        
        # 2. Check if the file exists
        if not file_path.exists():
            print(f"Error: File not found! -> {file_path}")
            print("Please ensure the 'data' folder exists in the project root.")
            return None
            
        print(f"Reading data: {file_path}")
        
        # 3. Read the Parquet File
        df = pd.read_parquet(file_path)
        
        print("Data loaded into memory successfully.")
        return df
        
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# This code block runs only when the script is executed directly
if __name__ == "__main__":
    
    # 1. Load the data
    data_frame = load_data()
    
    # 2. Check if data loading was successful
    if data_frame is not None:
        
        # 3. Display the first 5 rows
        print("\n--- DataFrame Head ---")
        print(data_frame.head())
        
        # 4. Get info about the DataFrame (columns, types, nulls)
        print("\n--- DataFrame Info ---")
        data_frame.info()
        
        # 5. Display the last 5 rows
        print("\n--- DataFrame Tail ---")
        print(data_frame.tail())