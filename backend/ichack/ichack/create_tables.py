import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="ichack"
)

mycursor = mydb.cursor()


def create_Companies_table():
    sql = "CREATE TABLE IF NOT EXISTS Companies (\
                company_id int,\
                name varchar(255),\
                logo_url varchar(255),\
                email varchar(255),\
                nr_people_recruited_from_website int, \
                sustainability_score float,\
                diversity_inclusive boolean,\
                description varchar(1024),\
                website_link varchar(255),\
                password varchar(255)\
        );"

    mycursor.execute(sql)
    mydb.commit()
    print("created companies table")


def create_People_table():
    sql = "CREATE TABLE IF NOT EXISTS People (\
                person_id int,\
                first_name varchar(255),\
                last_name varchar(255),\
                years_of_experience int,\
                email varchar(255),\
                former_company varchar(255),\
                former_role varchar(255),\
                locations varchar(255), \
                remote boolean,\
                linkedin varchar(255),\
                diversity_preferences_lgbtq boolean,\
                diversity_preferences_minority boolean,\
                diversity_preferences_disability boolean,\
                sustainability_preferences boolean,\
                laidoff_time DATE,\
                liked_roles varchar(2048),\
                profile_summary varchar(2048),\
                keywords_in_ps varchar(2048),\
                password varchar(255)\
        );"

    mycursor.execute(sql)
    mydb.commit()
    print("created people table")


def create_Roles_table():
    sql = "CREATE TABLE IF NOT EXISTS Roles (\
                company_id int, \
                name varchar(255),\
                description varchar(255),\
                location varchar(255),\
                remote boolean, \
                list_people_interested_in_role varchar(255),\
                embedding varchar(2048)\
        );"

    mycursor.execute(sql)
    mydb.commit()
    print("created Roles table")


if __name__ == "__main__":
    create_Companies_table()

    create_People_table()

    create_Roles_table()
