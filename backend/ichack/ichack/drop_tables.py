import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="ichack"
)

mycursor = mydb.cursor()


def drop_Companies_table():
    sql = "DROP TABLE IF EXISTS Companies;"

    mycursor.execute(sql)
    mydb.commit()
    print("dropped companies table")


def drop_People_table():
    sql = "DROP TABLE IF EXISTS People;"

    mycursor.execute(sql)
    mydb.commit()
    print("dropped people table")


def drop_Roles_table():
    sql = "DROP TABLE IF EXISTS Roles;"

    mycursor.execute(sql)
    mydb.commit()
    print("dropped Roles table")


if __name__ == "__main__":
    drop_Companies_table()

    drop_People_table()

    drop_Roles_table()
