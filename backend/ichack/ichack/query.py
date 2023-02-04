from mysql.connector import MySQLConnection, Error
from .python_mysql_dbconfig import read_db_config


def query_with_fetchall(query):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows
        # print("Total Row(s):", cursor.rowcount)
        # for row in rows:
        #    print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
