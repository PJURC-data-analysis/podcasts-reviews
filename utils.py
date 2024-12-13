import sqlite3
import pandas as pd
import numpy as np
from scipy import stats

def database_tables(connection: sqlite3.Connection) -> None:
    """Prints the tables of a sqlite database

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
    """
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    tables = connection.execute(query).fetchall()
    return [table[0] for table in tables]

def table_schema(connection: sqlite3.Connection, table_name: str) -> None:
    """Prints the schema of a sqlite table.

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
        table_name (str): The name of the table to print the schema for.
    """
    query = f"PRAGMA table_info({table_name})"
    table_schema = connection.execute(query).fetchall()
    print(f"Schema for table {table_name}:")
    for col_info in table_schema:
        print(col_info)
    print('\n')


def table_head(connection: sqlite3.Connection, table_name: str, n: int=5) -> None:
    """Prints the first n rows of a table.

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
        table_name (str): The name of the table to print the head for.
        n (int, optional): The number of rows to print. Defaults to 5.
    """
    query = f"SELECT * FROM {table_name} LIMIT {n}"
    df = pd.read_sql_query(query, connection)
    print(f"Head of table {table_name}:")
    pd.set_option('display.max_colwidth', 15)
    print(df.head(n))
    print('\n')


def check_null_values(connection: sqlite3.Connection, table_name: str):
    """Check null values within a table

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
        table_name (str): The name of the table to check for null values.
    Returns:
        None. Prints the rows with null values. If no rows with null values are found, it prints a message.
    """
    cursor = connection.cursor()

    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]

    # Generate SQL query dynamically
    query = f"SELECT * FROM {table_name} WHERE "
    for column_name in column_names:
        query += f"{column_name} IS NULL OR "
    query = query[:-4]  # Remove the last " OR "

    # Execute query
    cursor.execute(query)
    rows_with_nulls = cursor.fetchall()

    # Display results
    if len(rows_with_nulls) > 0:
        print("Rows with null values:")
        for row in rows_with_nulls:
            print(row)
    else:
        print(f"No rows with null values found for table {table_name}.")


def check_duplicates(connection: sqlite3.Connection, table_name: str, column_name: str):
    """Check for duplicates in the specified table column.

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
        table_name (str): The name of the table to check for duplicates.
        column_name (str): The name of the column to check for duplicates.
    Returns:
        None. Prints the duplicate values and their counts if any are found. Otherwise, it prints a message.
    """
    cursor = connection.cursor()

    # Query to check for duplicates
    query = f"SELECT {column_name}, COUNT(*) FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1;"

    # Execute query
    cursor.execute(query)
    duplicates = cursor.fetchall()

    # Display results
    if len(duplicates) > 0:
        print(f"{len(duplicates)} duplicate values found in table {table_name} column {column_name}:")
        for value, count in duplicates[:10]:
            print(f"Value: {value}, Count: {count}")
        print('...')
    else:
        print(f"No duplicate values found in table {table_name} column {column_name}")


def corr_ci(df: pd.DataFrame, col1: str, col2: str, conf_level: float=0.95) -> None:
    """Calculate the correlation coefficient for two variables. Assumed 95% confidence level by default.

    Args:
        df (pd.DataFrame): The DataFrame containing the variables.
        col1 (str): The name of the first variable.
        col2 (str): The name of the second variable.
        conf_level (float, optional): The confidence level to use for statistical inference.
    Returns:
        None. Prints the correlation coefficient, confidence interval and the p-value.
    """
    # Correlation coefficient & p-value
    corr, pval = stats.pearsonr(df[col1], df[col2])
    
    # Sample size & z-score
    n = len(df)
    z_score = np.abs(1 - (1 - conf_level) / 2)
    
    # Standard error
    se = 1 / np.sqrt(n - 3)
    z_score_category = np.arctanh(corr) / se
    
    # Confidence interval
    ci = np.tanh(np.array([np.arctanh(corr) - z_score_category * se,
                       np.arctanh(corr) + z_score_category * se]))
    
    # Print results
    print(f"Correlation coefficient: {corr:.2f}")
    print(f"95% confidence interval: [{ci[0]:.5f}, {ci[1]:.5f}]")
    print(f"p-value: {pval:.4f}")