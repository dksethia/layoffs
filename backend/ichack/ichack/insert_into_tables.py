import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="ichack"
)

mycursor = mydb.cursor()


def insert_into_Companies(tuples):
    sql = "INSERT INTO Companies (\
            company_id, \
            name, \
            website_link, \
            contact, \
            address, \
            nr_people_recruited_from_website, \
            logo_url, \
            sustainability_score, \
            diversity_inclusive, \
            description, \
            password,\
            email\
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = tuples
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


def insert_into_People(tuples):
    sql = "INSERT INTO People (\
            person_id, \
            first_name, \
            last_name, \
            email, \
            gender,\
            former_company, \
            linkedin, \
            remote, \
            locations, \
            diversity_preferences_lgbtq,\
            diversity_preferences_disability, \
            diversity_preferences_minority, \
            sustainability_preferences, \
            liked_roles, \
            former_role, \
            profile_summary, \
            keywords_in_ps, \
            years_of_experience, \
            password, \
            race\
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = tuples
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


def insert_into_Roles(tuples):
    sql = "INSERT INTO Roles (\
            name, \
            description, \
            company_id, \
            location, \
            remote, \
            list_people_interested_in_role, \
            embedding\
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = tuples
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
