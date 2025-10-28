# Crypto Portfolio Data Pipeline & Modeling

## Project Overview

This project is a complete data pipeline and analysis framework for cryptocurrency data. Its goal is to systematically download, store, and process high-frequency (5-minute) OHLCV data for the top 20 cryptocurrencies by market cap.

The data is fetched from public APIs (CoinGecko and CryptoCompare) and stored in a local **PostgreSQL** database. The pipeline is designed to be **idempotent**, meaning it can be run repeatedly without creating duplicate data entries.

The resulting dataset provides a robust, local, and queryable foundation for advanced time-series analysis, backtesting trading strategies, and developing deep learning (PyTorch) models for price forecasting or portfolio management.

-----

## Core Features

  * **Data Sourcing**: Fetches the top 20 coins by market cap (USD) from CoinGecko.
  * **Historical Backfill**: Downloads the previous 90 days of 5-minute OHLCV data for each coin from CryptoCompare.
  * **Robust Storage**: Stores all time-series data in a local PostgreSQL database.
  * **Idempotent Upserts**: Safely inserts or updates data using `ON CONFLICT` to prevent duplicates, making the pipeline safe to re-run.
  * **Modern Python Packaging**: Built as an installable `src/` style package.
  * **Modeling Ready**: Includes scaffolding for time-series analysis and PyTorch (deep learning) models.

## Tech Stack

  * **Python 3.9+**
  * **PyTorch**: For all deep learning models.
  * **PostgreSQL**: For time-series data storage.
  * **psycopg**: Python driver for PostgreSQL.
  * **pandas** & **polars**: For data manipulation and analysis.
  * **requests**: For all API calls.
  * **pydantic-settings**: For secure management of configuration and API keys.

-----

## Project Structure

```
crypto_portfolio_project/
├── .env                  # Local secrets (API keys, DB URL)
├── .env.example          # Template for .env
├── .gitignore
├── pyproject.toml        # Project definition and dependencies
├── README.md             # This file
├── notebooks/            # Jupyter notebooks for exploration
│   └── 01_explore_data.ipynb
├── scripts/              # Runnable entrypoints
│   ├── run_backfill.py   # Main script to run the full pipeline
│   ├── run_analysis.py   # Script to train/run a model
│   └── setup_database.py # Helper to create tables
├── sql/
│   └── 01_create_tables.sql  # SQL schema definition
├── src/
│   └── crypto_portfolio/   # The installable Python package
│       ├── __init__.py
│       ├── clients/          # API clients (CoinGecko, CryptoCompare)
│       │   ├── __init__.py
│       │   ├── coingecko.py
│       │   └── cryptocompare.py
│       ├── core/             # Orchestration logic
│       │   ├── __init__.py
│       │   └── backfill.py   # Main pipeline coordination
│       ├── db/               # Database interactions
│       │   ├── __init__.py
│       │   ├── connection.py # Connection/session management
│       │   └── operations.py # Upsert/query logic
│       ├── analysis/         # Modeling and analysis code
│       │   ├── __init__.py
│       │   ├── deep_learning.py
│       │   └── time_series.py
│       └── config.py         # Loads settings from .env
│
└── tests/                  # Unit tests
    └── ...
```

-----

## Setup & Installation

Follow these steps to set up your local environment.

### 1\. Clone Repository

```bash
git clone <your-repo-url>
cd crypto_portfolio_project
```

### 2\. Create Virtual Environment

```bash
# Create the environment
python3 -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# (Windows)
# .\venv\Scripts\activate
```

### 3\. Install Project & Dependencies

Install the project in "editable" mode (`-e`). This reads the `pyproject.toml` file, installs all dependencies, and links your `src/` folder to the environment.

```bash
pip install -e ".[dev]"
```

### 4\. Set Environment Variables

Copy the example file to create your local secret file.

```bash
cp .env.example .env
```

Now, **edit the `.env` file** with your credentials:

```env
# .env
DATABASE_URL="postgresql://username:password@localhost:5432/crypto_db"
CRYPTOCOMPARE_API_KEY="your_api_key_from_cryptocompare_here"
```

### 5\. Setup PostgreSQL Database

Make sure you have PostgreSQL installed and running.

1.  **Create the Database:**

    ```sql
    -- Run this in psql or your DB GUI
    CREATE DATABASE crypto_db;
    ```

2.  **Create the Tables:**
    Run the SQL script to create the `crypto_ohlcv_5min` and `crypto_symbols` tables.

    ```bash
    # Run this from your terminal
    psql -d crypto_db -U your_username -f sql/01_create_tables.sql
    ```

-----

## Usage

### 1\. Run the Full Data Backfill

This is the main script. It will:

1.  Fetch the top 20 coins.
2.  Iterate through each coin.
3.  Fetch 90 days of 5-min data.
4.  Upsert all data into your database.

<!-- end list -->

```bash
python scripts/run_backfill.py
```

### 2\. Run Analysis or Model Training

This script (which you will build) will load data from the database and run a PyTorch model.

```bash
python scripts/run_analysis.py
```

### 3\. Explore Data

Use Jupyter Lab to run notebooks in the `notebooks/` folder for ad-hoc exploration.

```bash
jupyter lab
```