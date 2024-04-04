CREATE SCHEMA IF NOT EXISTS coincap_bitcoin;


CREATE TABLE IF NOT EXISTS coincap_bitcoin.bitcoin_price_tracker (
    id INTEGER,
    timestamp TIMESTAMP,
    rank INTEGER,
    symbol VARCHAR(10),
    name VARCHAR(255),
    supply NUMERIC,
    max_supply NUMERIC,
    market_cap_usd NUMERIC,
    volume_usd_24_hr NUMERIC,
    price_usd NUMERIC,
    change_percent_24_hr NUMERIC,
    vwap_24_hr NUMERIC,
    explorer VARCHAR(255)
);




CREATE TABLE coincap_bitcoin.bitcoin_kpi (
    timestamp timestamp,
    current_price numeric(18,0),
    price_change_percentage numeric(38,2),
    supply numeric(18,0),
    max_supply numeric(18,0),
    percentage_of_max_supply_mined numeric(38,2),
    volatility numeric(38,2),
    moving_average_10_days numeric(18,0),
    market_dominance numeric(38,2),
    vwap_24_hr numeric(18,0),
    vwap_crossing character varying(10)
);
