import sqlite3

connection = sqlite3.connect("babar_tables")
cursor = connection.cursor()

sql_file = open("babar3_modified.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)