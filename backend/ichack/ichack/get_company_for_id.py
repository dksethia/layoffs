import json
from .query import query_with_fetchall

def get_company_for_id(json_data):

    dict_data = json.loads(json_data)

    comp_id = dict_data['id']

    roles_for_company = query_with_fetchall(f"SELECT * FROM Companies WHERE company_id={comp_id}")

    return roles_for_company


print(get_company_for_id('{"id":4}'))