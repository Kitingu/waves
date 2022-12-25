import os
import pyodbc
from dotenv import load_dotenv

load_dotenv() 

DRIVER_NAME =  os.getenv("DB_DRIVER_NAME")
DB_SERVER_NAME = os.getenv("DB_SERVER_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def connectDb():
    conn = pyodbc.connect(
        f"DRIVER={DRIVER_NAME};SERVER={DB_SERVER_NAME};PORT=1433;DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD};Trusted_Connection=yes")
    print("connection created successfully")
    return conn


def query(query):
    conn = connectDb()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return conn.commit()
        conn.close()
    except Exception as e:
        print("sql-error:",e)
        conn.rollback()
        conn.close()

    