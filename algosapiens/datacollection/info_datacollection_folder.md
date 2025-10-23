The files within this folder contain many files and processes related to data collection, such as fetching data via the APIs of Binance and other applications, converting this data into PARQUET.

Additionally, the details and descriptions of the files contained in this folder are available below.

----------!!!----------

- `data_collection.py` -  Fetches the required amount of data from the Binance APIs and saves it in PARQUET format into the data folder in the parent directory.

- `data_read.py` - This script is used to read PARQUET formatted files located in the data folder in the parent directory. It displays the row/column properties (metadata) of the files, as well as the first 5 (head) and the last 5 (tail) rows of data.
