from env import db_url
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import pandas as pd


def grab_sql(db, query, filename):
    """
    Grab data from Codeup's MySQL server utilizing db_url with credentials from a personal env file.
    Check if filename file exists. If it does not exist, it will create one.

    This function selects ALL data from a table with no limit on size.

    Args:
        db (str): The name of the database.
        table (str): The name of the table within that database.
        filename (str): The name of the file to be created.
        query (str, optional): The SQL query to execute. Defaults to "SELECT * FROM <table>".

    Returns:
        pandas.DataFrame: A pandas dataframe containing the data from the selected table.
    """
    connection = db_url(db)
    df = pd.read_sql(query, connection)
    df.to_csv(filename, index=False)
    return df


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


def get_iris_data():
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
        SELECT species.species_name, measurements.*
        FROM measurements
        JOIN species
        ON measurements.species_id = species.species_id;"""
        connection = db_url("iris_db")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df


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


def split_data(df, target):
    """
    take in a DataFrame and return train, validate, and test DataFrames; stratify on a specified variable.
    return train, validate, test DataFrames.
    """
    train_validate, test = train_test_split(
        df, test_size=0.2, random_state=123, stratify=df[target]
    )
    train, validate = train_test_split(
        train_validate, test_size=0.3, random_state=123, stratify=train_validate[target]
    )
    print(f"train: {len(train)} ({round(len(train)/len(df), 2)*100}% of {len(df)})")
    print(
        f"validate: {len(validate)} ({round(len(validate)/len(df), 2)*100}% of {len(df)})"
    )
    print(f"test: {len(test)} ({round(len(test)/len(df), 2)*100}% of {len(df)})")

    return train, validate, test
