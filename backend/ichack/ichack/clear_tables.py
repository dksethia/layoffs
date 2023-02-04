import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="ichack"
)

mycursor = mydb.cursor()


def delete_from_Companies():
    sql = "DELETE FROM Companies"
    mycursor.execute(sql)
    mydb.commit()
    print("deleted from Companies")


def delete_from_People():
    sql = "DELETE FROM People"

    mycursor.execute(sql)
    mydb.commit()
    print("deleted from People")


def delete_from_Roles():
    sql = "DELETE FROM Roles"

    mycursor.execute(sql)
    mydb.commit()
    print("deleted from Roles")


if __name__ == "__main__":
    delete_from_Companies()

    delete_from_People()

    delete_from_Roles()
