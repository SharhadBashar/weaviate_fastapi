import os
import json
import psycopg2
from psycopg2 import extras

from helper import *
from constants import *

class Database:
    def __init__(self):
        database_info = read_json(os.path.join(PATH_CONFIG, DB_CONFIG_CK))
        self.db_url = os.getenv('DATABASE_URL')
        # self.db_url = database_info['db_url']
        self.conn = psycopg2.connect(self.db_url)

    def insert_df(self, df, table_name):
        try:
            # Ensure DataFrame is not empty
            if df.empty:
                print('The DataFrame is empty. No data to insert.')
                return
            with psycopg2.connect(self.db_url) as conn:
                with conn.cursor() as cursor:
                    # Prepare data and SQL query
                    tuples = [tuple(x) for x in df.to_numpy()]
                    columns = ','.join(list(df.columns))
                    placeholders = ','.join(['%s'] * len(df.columns))
                    query = """INSERT INTO {} 
                               ({}) VALUES ({})
                            """.format(
                                table_name,
                                columns,
                                placeholders
                            )
                    extras.execute_batch(cursor, query, tuples)
                    conn.commit()
                    print('Dataframe inserted successfully into CockroachDB')
        except psycopg2.DatabaseError as e:
            print(f'Database error occurred: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')
            
    def insert_df(self, df, table_name):
        conn = self.conn
        tuples = [tuple(x) for x in df.to_numpy()]
        columns = ','.join(list(df.columns))
        placeholders = ','.join(['%s'] * len(df.columns))
        query = """INSERT INTO 
                    {} 
                    ({}) 
                   VALUES 
                    ({})
                """.format(
                    table_name,
                    columns,
                    placeholders
                )
        cursor = conn.cursor()
        extras.execute_batch(cursor, query, tuples)
        conn.commit()
        cursor.close()
