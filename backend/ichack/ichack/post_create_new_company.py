import json
from .query import query_with_fetchall
from .insert_into_tables import insert_into_Companies

def post_create_company(json_input):
    dict_input = json.loads(json_input)

    n = query_with_fetchall(f"SELECT MAX(company_id) FROM Companies")[0]['MAX(company_id)']+1

    return_tuple = (
        n,
        dict_input['name'],
        dict_input['website'],
        "",
        dict_input['address'],
        0,
        dict_input['logo_url'],
        dict_input['sus_score'],
        dict_input['diversity_inc'],
        dict_input['description'],
        dict_input['password'],
        dict_input['email']
    )

    insert_into_Companies([return_tuple])

    print("Successfully added a new company!")

            # company_id, \
            # name, \
            # website_link, \
            # contact, \
            # address, \
            # nr_people_recruited_from_website, \
            # logo_url, \
            # sustainability_score, \
            # diversity_inclusive, \
            # description, \
            # password,\
            # email\