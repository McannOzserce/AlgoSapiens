The file within this folder contains processes related to data analysis and processing, specifically converting raw data into calculated metrics stored in PARQUET format.

Additionally, the details and description of the file contained in this folder are available below.

----------!!!----------

-`calculate_real_body.py` - Reads the `PARQUET` file located in the data folder in the parent directory. It `calculates the percentage change (real body) using the (Close - Open) / Open formula` on the data and saves this processed data as a new `PARQUET` file.