import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


def create_connection():

    try:

        connection = mysql.connector.connect(

            host=os.getenv("MYSQL_HOST"),

            port=int(os.getenv("MYSQL_PORT")),

            user=os.getenv("MYSQL_USER"),

            password=os.getenv("MYSQL_PASSWORD"),

            database=os.getenv("MYSQL_DB")

        )

        print("Database Connected Successfully!")

        return connection


    except mysql.connector.Error as e:

        print("Database Connection Error:", e)

        return None



def fetch_one(query, params=None):

    connection = create_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(query, params or ())

    result = cursor.fetchone()

    cursor.close()

    connection.close()

    return result



def fetch_all(query, params=None):

    connection = create_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(query, params or ())

    result = cursor.fetchall()

    cursor.close()

    connection.close()

    return result



def execute_query(query, params=None):

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute(query, params or ())

    connection.commit()

    cursor.close()

    connection.close()



def execute_insert(query, params=None):

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute(query, params or ())

    connection.commit()

    last_id = cursor.lastrowid

    cursor.close()

    connection.close()

    return last_id