# A program that connects to a SQL DATABASE.
import sqlite3
print("creating connecting ...")
conn = sqlite3.connect('mydatabase.db')
conn . close()
print("\nThe SQLite connection is closed")
