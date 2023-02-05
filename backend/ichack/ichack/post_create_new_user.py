import json
from .embedding import create_embedding
from .query import query_with_fetchall
from .insert_into_tables import insert_into_People

def post_create_user(json_input):
    dict_input = json.loads(json_input)

    n = query_with_fetchall(f"SELECT MAX(person_id) FROM People")[0]['MAX(person_id)']+1

    return_tuple = (
        n,
        dict_input['firstName'],
        dict_input['lastName'],
        dict_input['email'],
        dict_input['gender'],
        dict_input['formerCompany'],
        dict_input['linkedin'],
        dict_input['remote'],
        dict_input['locations'],
        dict_input['diversity_preferences_lgbtq'],
        dict_input['diversity_preferences_disability'],
        dict_input['diversity_preferences_minority'],
        dict_input['liked_roles'],
        dict_input['former_role'],
        dict_input['profile_summary'],
        create_embedding(dict_input['profile_summary']),
        dict_input['experience'],
        dict_input['password'],
        dict_input['race']
    )

    insert_into_People([return_tuple])

    print("Successfully added a new user!")


#              person_id, \
#             first_name, \
#             last_name, \
#             email, \
#             gender,\
#             former_company, \
#             linkedin, \
#             remote, \
#             locations, \
#             diversity_preferences_lgbtq,\
#             diversity_preferences_disability, \
#             diversity_preferences_minority, \
#             sustainability_preferences, \
#             liked_roles, \
#             former_role, \
#             profile_summary, \
#             keywords_in_ps, \
#             years_of_experience, \
#             password, \
#             race\