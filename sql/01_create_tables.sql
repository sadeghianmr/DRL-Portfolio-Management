-- Creates the main table for 5-minute OHLCV data
CREATE TABLE IF NOT EXISTS crypto_ohlcv_5min (
    symbol VARCHAR(20) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    open NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    volume NUMERIC NOT NULL,
    
    -- This constraint ensures that you can never have two
    -- rows for the same symbol at the same time.
    -- This is the key to idempotency.
    PRIMARY KEY (symbol, timestamp)
);

-- Optional: Create an index for faster time-series queries
CREATE INDEX IF NOT EXISTS idx_crypto_ohlcv_symbol_time 
ON crypto_ohlcv_5min (symbol, timestamp DESC);

-- Optional: Create a table for symbol metadata
CREATE TABLE IF NOT EXISTS crypto_symbols (
    id VARCHAR(100) PRIMARY KEY, -- e.g., 'bitcoin' from coingecko
    symbol VARCHAR(20) NOT NULL,   -- e.g., 'BTC'
    name VARCHAR(100) NOT NULL,
    market_cap_rank INT,
    last_updated TIMESTAMPTZ
);