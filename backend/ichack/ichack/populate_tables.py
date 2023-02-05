from insert_into_tables import *
import csv


def prepare_row(row):
    for i in range(len(row)):
        if row[i] == "True":
            row[i] = True
        if row[i] == "False":
            row[i] = False
    return tuple(row)


if __name__ == "__main__":
    roles = [prepare_row(row) for row in csv.reader(open("ichack/roles.csv", "rU"))][1:]
    insert_into_Roles(roles)

    users = [
        prepare_row(row[1:]) for row in csv.reader(open("ichack/users_extended.csv", "rU"))
    ][1:]
    insert_into_People(users)

    companies = [
        prepare_row(row[2:]) for row in csv.reader(open("ichack/companies.csv", "rU"))
    ][1:]
    insert_into_Companies(companies)
