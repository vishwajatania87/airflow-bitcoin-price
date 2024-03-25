# Airflow Bitcoin Data Analysis Project

This project utilizes Apache Airflow to automate the collection and analysis of Bitcoin price data. It consists of two DAGs:

1. `coincaptoyb_dag`: Fetches Bitcoin price data from the CoinCap API and uploads it to a PostgreSQL database. Upon successful execution, it triggers another DAG for further analysis.

2. `bitcoin_kpi_dag`: Calculates key performance indicators (KPIs) related to Bitcoin using data stored in the PostgreSQL database. It computes various metrics such as price change percentage, volatility, and market dominance.

## Prerequisites

Before running these DAGs, ensure that you have the following:

- Apache Airflow installed and configured
- PostgreSQL database set up with appropriate tables (`coincap_bitcoin.bitcoin_price_tracker` and `coincap_bitcoin.bitcoin_kpi`)
- Necessary connections configured in Airflow (`ybconnection` for PostgreSQL)

## DAG Descriptions

### 1. coincaptoyb_dag

- **Purpose**: Fetches Bitcoin price data from the CoinCap API and uploads it to a PostgreSQL database.
- **Tasks**:
  - `fetch_and_upload_bitcoin_price`: PythonOperator task to fetch data from the API and upload it to PostgreSQL.
  - `execute_sql_task`: TriggerDagRunOperator to trigger the `bitcoin_kpi_dag` upon successful data upload.
- **Schedule Interval**: Runs every 5 minutes.

### 2. bitcoin_kpi_dag

- **Purpose**: Calculates key performance indicators (KPIs) related to Bitcoin using data stored in PostgreSQL.
- **Tasks**:
  - `execute_sql_task`: PostgresOperator task to execute SQL queries for KPI calculation and insertion.
- **Dependencies**: Depends on successful execution of the `coincaptoyb_dag`.
- **Schedule Interval**: None (not scheduled to run periodically).

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/airflow-bitcoin-analysis.git
