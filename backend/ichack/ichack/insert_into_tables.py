import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="ichack"
)

mycursor = mydb.cursor()


def insert_into_Companies(tuple):
    sql = "INSERT INTO Companies (\
            company_id, \
            name, \
            logo_url, \
            email, \
            nr_people_recruited_from_website, \
            sustainability_score, \
            diversity_inclusive, \
            description, \
            website_link, \
            password\
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = tuple
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


def insert_into_People(tuple):
    sql = "INSERT INTO People (\
            person_id, \
            first_name, \
            last_name, \
            years_of_experience, \
            email, \
            former_company, \
            former_role, \
            locations, \
            remote, \
            linkedin, \
            diversity_preferences_lgbtq,\
            diversity_preferences_minority, \
            diversity_preferences_disability, \
            sustainability_preferences, \
            laidoff_time, \
            liked_roles, \
            profile_summary, \
            keywords_in_ps, \
            password\
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = tuple
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


def insert_into_Roles(tuple):
    sql = "INSERT INTO Roles (\
            company_id, \
            name, \
            description, \
            location, \
            remote, \
            list_people_interested_in_role, \
            embedding\
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = tuple
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


if __name__ == "__main__":
    pass
