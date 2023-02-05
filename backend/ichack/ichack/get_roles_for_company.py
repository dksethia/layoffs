import json
from .query import query_with_fetchall



def get_roles_for_company(comp_id):
    
    # dict_input = json.loads(json_input)

    # comp_id = dict_input['id']

    print(comp_id)

    roles_for_company = query_with_fetchall(f"SELECT role_id, name, description, location, remote, list_people_interested_in_role as ppl_list FROM Roles WHERE company_id={comp_id}")
    #print(roles_for_company)
    
    if roles_for_company is None:
        return {"items":[]}


    for i in range(len(roles_for_company)):
        roles_for_company[i]['ppl_list'] = roles_for_company[i]['ppl_list'].split(';')
    
    return {"items":roles_for_company}

