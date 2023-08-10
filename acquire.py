from env import db_url
import pandas as pd
import os


def grab_sql(db, table, filename):
    """
    grab sql will grab data from codeups mysql server utilizing db_url
    with credentials from a personal env file. It will check if filename file exists.
    If it does not exist, it will create one.

    This will only select ALL data from a table with no limit on size.

    arguments: db is the database
               table is the table within that database
               filename is what the file will be named

    return: a pandas dataframe
    """
    query = "SELECT * FROM " + table + ";"
    connection = db_url(db)
    df = pd.read_sql(query, connection)
    df.to_csv(filename, index=False)
    return df


# 1. Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame.
# Obtain your data from the Codeup Data Science Database.


def get_titanic_data():
    """
    get titanic data will query the titanic database and return all the data within

    arguments: none

    return: a pandas dataframe
    """
    filename = "titanic.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = "SELECT * FROM passengers"
        connection = db_url("titanic_db")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df


# def get_titanic_data():
#     grab_data('titanic_db', 'passengers')
#     return df

# 2. Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame.
# The returned data frame should include the actual name of the species in addition to the species_ids.
# Obtain your data from the Codeup Data Science Database.


def get_iris():
    """
    get iris will query the iris database and return all the data within

    arguments: none

    return: a pandas dataframe
    """
    filename = "iris.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT DISTINCT measurements.*, species.species_name
        FROM measurements
        JOIN species
        ON measurements.species_id = species.species_id;"""
        connection = db_url("iris_db")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df


# 3. Make a function named get_telco_data that returns the data from the telco_churn database in SQL.
# In your SQL, be sure to join contract_types, internet_service_types, payment_types tables with the customers table,
# so that the resulting dataframe contains all the contract, payment, and internet service options.
# Obtain your data from the Codeup Data Science Database.


def get_telco_data():
    """
    get telco data will query the telco database and return all the relevant churn data within

    arguments: none

    return: a pandas dataframe
    """
    filename = "telco.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT *
        FROM customers
        JOIN contract_types
        ON customers.contract_type_id = contract_types.contract_type_id
        JOIN internet_service_types
        ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
        JOIN payment_types
        ON customers.payment_type_id = payment_types.payment_type_id;"""
        connection = db_url("telco_churn")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df


# 4. Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time to add caching to them.
# To do this, edit the beginning of the function to check for the local filename of telco.csv, titanic.csv, or iris.csv.
# If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe,
# then write the dataframe to a .csv file with the appropriate name.
