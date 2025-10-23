# AlgoSapiens Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-10-22

### Added

- **Project Initialization:** The repository `AlgoSapiens` was created.
- **Initial Documentation:**
  - `README.md`: Added the core mission, "education-first" philosophy, and multi-phase development plan.
  - `CHANGELOG.md`: This file was created to track all future versions and notable changes.
- **Initial `.gitignore`:** Added a standard Python `.gitignore` file to exclude common temporary files (like `__pycache__` and virtual environments) from version control.

## [0.1.0] - 2025-10-23

### Added
- Added the core data pipeline scripts (`datacollection/`) as defined in Phase 1.
- `data_collection.py`: New script to fetch bulk historical candle data from Binance API.
- `data_read.py`: New script to read data from disk into a pandas DataFrame.
- Chose `.parquet` file format over CSV/Excel for high-speed I/O performance and scalability (tested successfully with 50k rows).

### Changed
- **CRITICAL:** Updated `data_collection.py` to pull `quote_asset_volume` (e.g., USDT value) instead of `volume` (e.g., BTC amount). This is a much more accurate signal for financial power.
- Renamed `quote_asset_volume` to `volume` within the DataFrame for consistent use in future features.

### Fixed
- Added `.DS_Store` (macOS system files) to `.gitignore` to prevent repository clutter.
