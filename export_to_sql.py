import psycopg2
from dotenv import load_dotenv
import dotenv
import os
import pandas as pd

def export_to_sql_from_csv(file_path, table_name):
    # file_path = os.environ.get('FILE_PATH')

    user = os.environ.get('DB_CBP_USERNAME')
    password = os.environ.get('DB_CBP_PASSWORD')

    # Read in Excel File

    # Define connection parameters
    conn = psycopg2.connect(
        dbname="Customs and Border Protection",
        user=user,
        password=password,
        host="localhost",  # Change if remote
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS ''' + str(table_name) + ''' (
        FISCAL_YEAR TEXT,
        MONTH_GROUPING TEXT,
        MONTH TEXT,
        COMPONENT TEXT,
        LAND_BORDER_REGION TEXT,
        AREA_RESP TEXT,
        AOR TEXT,
        DEMOGRAPHIC TEXT,
        CITIZENSHIP TEXT,
        TITLE_AUTH TEXT,
        ENCOUNTER_TYPE TEXT,
        ENCOUNTER_COUNT INT
    );
    '''

    # drop_query = '''
    # DROP TABLE nationwide_encounters_fy22_25'''
    # cur.execute(drop_query)
    cur.execute(create_table_query)

    # Read Excel File
    df = pd.read_csv(file_path)
    print(df.head)
    print(df.columns)

    insert_query = '''
    INSERT INTO  ''' + str(table_name) + '''(
        FISCAL_YEAR,
        MONTH_GROUPING,
        MONTH,
        COMPONENT,
        LAND_BORDER_REGION,
        AREA_RESP,
        AOR,
        DEMOGRAPHIC,
        CITIZENSHIP,
        TITLE_AUTH,
        ENCOUNTER_TYPE,
        ENCOUNTER_COUNT)

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    '''

    # data = df.values.tolist()

    data = [tuple(row) for row in df.itertuples(index=False, name=None)]
    print(data[:5])

    # Execute a test query
    cur.executemany(insert_query, data[1:])
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()

def export_to_sql_from_df(df, table_name):
    # file_path = os.environ.get('FILE_PATH')

    user = os.environ.get('DB_CBP_USERNAME')
    password = os.environ.get('DB_CBP_PASSWORD')

    # Read in Excel File

    # Define connection parameters
    conn = psycopg2.connect(
        dbname="Customs and Border Protection",
        user=user,
        password=password,
        host="localhost",  # Change if remote
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS ''' + str(table_name) + ''' (
        FISCAL_YEAR TEXT,
        MONTH_GROUPING TEXT,
        MONTH TEXT,
        COMPONENT TEXT,
        LAND_BORDER_REGION TEXT,
        AREA_RESP TEXT,
        AOR TEXT,
        DEMOGRAPHIC TEXT,
        CITIZENSHIP TEXT,
        TITLE_AUTH TEXT,
        ENCOUNTER_TYPE TEXT,
        ENCOUNTER_COUNT INT
    );
    '''

    # drop_query = '''
    # DROP TABLE nationwide_encounters_fy22_25'''
    # cur.execute(drop_query)
    cur.execute(create_table_query)

    # Read Excel File
    # df = pd.read_csv(file_path)
    print(df.head)
    print(df.columns)

    insert_query = '''
    INSERT INTO  ''' + str(table_name) + '''(
        FISCAL_YEAR,
        MONTH_GROUPING,
        MONTH,
        COMPONENT,
        LAND_BORDER_REGION,
        AREA_RESP,
        AOR,
        DEMOGRAPHIC,
        CITIZENSHIP,
        TITLE_AUTH,
        ENCOUNTER_TYPE,
        ENCOUNTER_COUNT)

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    '''

    # data = df.values.tolist()

    data = [tuple(row) for row in df.itertuples(index=False, name=None)]
    print(data[:5])

    # Execute a test query
    cur.executemany(insert_query, data[1:])
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()
