import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="ichack"
)

mycursor = mydb.cursor()


def create_Companies_table():
    sql = "CREATE TABLE IF NOT EXISTS Companies (\
                company_id int,\
                name varchar(500),\
                website_link varchar(500),\
                contact varchar(500),\
                address text,\
                nr_people_recruited_from_website int, \
                logo_url varchar(500),\
                sustainability_score float,\
                diversity_inclusive boolean,\
                description text,\
                password varchar(500)\
        );"

    mycursor.execute(sql)
    mydb.commit()
    print("created companies table")


def create_People_table():
    sql = "CREATE TABLE IF NOT EXISTS People (\
                person_id int,\
                first_name varchar(500),\
                last_name varchar(500),\
                email varchar(500),\
                gender varchar(500),\
                former_company varchar(500),\
                linkedin varchar(500),\
                remote boolean,\
                locations text, \
                diversity_preferences_lgbtq boolean,\
                diversity_preferences_minority boolean,\
                diversity_preferences_disability boolean,\
                sustainability_preferences boolean,\
                laidoff_time DATE,\
                liked_roles text,\
                former_role varchar(500),\
                profile_summary text,\
                keywords_in_ps text,\
                years_of_experience int,\
                password varchar(500)\
        );"

    mycursor.execute(sql)
    mydb.commit()
    print("created people table")


def create_Roles_table():
    sql = "CREATE TABLE IF NOT EXISTS Roles (\
                name varchar(500),\
                description text,\
                company_id int, \
                location varchar(500),\
                remote boolean, \
                list_people_interested_in_role text,\
                embedding text\
        );"

    mycursor.execute(sql)
    mydb.commit()
    print("created Roles table")


if __name__ == "__main__":
    create_Companies_table()

    create_People_table()

    create_Roles_table()
