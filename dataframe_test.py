import sqlite3
import pandas as pd

conn = sqlite3.connect('babar_tables')

sql_query = pd.read_sql_query('''
                               SELECT
                               *
                               FROM babar_server_customer
                               ''', conn)

df = pd.DataFrame(sql_query, columns=['id', 'firstname', 'lastname', 'nickname', 'email', 'year'])
print(df)