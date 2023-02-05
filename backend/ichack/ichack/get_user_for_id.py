import json
from .query import query_with_fetchall

def get_user_for_id(user_id):

    # dict_data = json.loads(json_data)

    # comp_id = dict_data['id']

    user = query_with_fetchall(f"SELECT * FROM People WHERE person_id={user_id}")
    print(user)
    return user


# print(get_company_for_id('{"id":4}'))