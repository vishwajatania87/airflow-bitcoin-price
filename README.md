# Airflow Bitcoin Price DAG

This project contains an Airflow DAG (Directed Acyclic Graph) for fetching the current price of Bitcoin from an API and storing it in a PostgreSQL database table.

## Overview

This Airflow DAG fetches the current price of Bitcoin from the CoinCap API at regular intervals and inserts it into a PostgreSQL database table. It demonstrates a simple data pipeline workflow using Apache Airflow.

## Prerequisites

Before running the DAG, ensure you have the following prerequisites installed:

- Apache Airflow
Set an Airflow Variable named dbconn to store a SQLAlchemy PostgreSQL URL using either the Airflow UI and CLI:

Using the Airflow UI:
Navigate to the Variables Page:

Open your web browser and go to the Airflow web interface.
Click on the "Admin" menu in the top navigation bar.
From the dropdown menu, select "Variables".
Add a New Variable:

On the Variables page, click on the "Create" button.
Enter the following details:
Key: dbconn
Value: Your SQLAlchemy PostgreSQL URL (e.g., postgresql://username:password@hostname:port/database_name)
Click on the "Save" button to create the variable.

Using the Airflow CLI:
Open Terminal or Command Prompt:

Open your terminal or command prompt.
Set the Variable:

Use the following command to set the variable using the Airflow CLI:
airflow variables set dbconn 'postgresql://username:password@hostname:port/database_name'

Replace the placeholders (username, password, hostname, port, database_name) with your PostgreSQL connection details.
Verify:

To verify that the variable has been set, you can use the following command:
airflow variables get dbconn

- Python packages listed in `requirements.txt`
- Access to a PostgreSQL database
- Run the sql located in 'ddl/create_bitcoin_price.sql' in your PostgreSQL database and have the table ready to land the data. 

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/vishwajatania87/airflow-bitcoin-price.git
