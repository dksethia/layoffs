import json
from .query import query_with_fetchall



def get_roles_for_company(json_input):
    
    dict_input = json.loads(json_input)

    comp_id = dict_input['id']

    roles_for_company = query_with_fetchall(f"SELECT name, description, location, remote, list_people_interested_in_role as ppl_list FROM Roles WHERE company_id={comp_id}")
    for i in range(len(roles_for_company)):
        roles_for_company[i]['ppl_list'] = roles_for_company[i]['ppl_list'].split(';')
    
    return {"items":roles_for_company}

