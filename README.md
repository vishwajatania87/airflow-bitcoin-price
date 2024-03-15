# Airflow Bitcoin Price DAG

This project contains an Airflow DAG (Directed Acyclic Graph) for fetching the current price of Bitcoin from an API and storing it in a PostgreSQL database table.

## Overview

This Airflow DAG fetches the current price of Bitcoin from the CoinCap API at regular intervals and inserts it into a PostgreSQL database table. It demonstrates a simple data pipeline workflow using Apache Airflow.

## Prerequisites

Before running the DAG, ensure you have the following prerequisites installed:

- Apache Airflow

- Set Airflow Variable for Database connection Using Airflow UI or CLI


 Using the Airflow UI:

1. **Navigate to the Variables Page**:
   - Open your web browser and go to the Airflow web interface.
   - Click on the "Admin" menu in the top navigation bar.
   - From the dropdown menu, select "Variables".

2. **Add a New Variable**:
   - On the Variables page, click on the "Create" button.
   - Enter the following details:
     - Key: `dbconn`
     - Value: Your PostgreSQL URL connection string (e.g., `postgresql://username:password@hostname:port/database_name`)
   - Click on the "Save" button to create the variable.

Using the Airflow CLI:

1. **Open Terminal or Command Prompt**:
   - Open your terminal or command prompt.

2. **Set the Variable**:
   - Use the following command to set the variable using the Airflow CLI:
     ```bash
     airflow variables set dbconn 'postgresql://username:password@hostname:port/database_name'
     ```
     Replace the placeholders (`username`, `password`, `hostname`, `port`, `database_name`) with your PostgreSQL connection details.

3. **Verify**:
   - To verify that the variable has been set, you can use the following command:
     ```bash
     airflow variables get dbconn
     ```
   - This command should return the value of the `dbconn` variable that you just set.


- Python packages listed in `requirements.txt`
- Access to a PostgreSQL database
- Run the sql located in 'ddl/create_bitcoin_price.sql' in your PostgreSQL database and have the table ready to land the data. 

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/vishwajatania87/airflow-bitcoin-price.git
