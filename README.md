# Airflow Bitcoin Price DAG

This project contains an Airflow DAG (Directed Acyclic Graph) for fetching the current price of Bitcoin from an API and storing it in a PostgreSQL database table.

## Overview

This Airflow DAG fetches the current price of Bitcoin from the CoinCap API at regular intervals and inserts it into a PostgreSQL database table. It demonstrates a simple data pipeline workflow using Apache Airflow.

## Prerequisites

Before running the DAG, ensure you have the following prerequisites installed:

- Apache Airflow
- Python packages listed in `requirements.txt`
- Access to a PostgreSQL database
- Run the DDL.sql in your PostgreSQL database and have the table ready to land the data. 

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/vishwajatania87/airflow-bitcoin-price.git
