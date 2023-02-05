from .encoding_filter import enc_filter
from .query import query_with_fetchall

def get_roles_for_user_query(text):
    
    res = []

    roles = query_with_fetchall(f"SELECT * FROM Roles;")
    companies = query_with_fetchall(f"SELECT * FROM Companies")

    roles = sorted(roles, key=lambda x: -enc_filter(x['embedding'], x['name'], text))[:10]
    rel_comps = [companies[x['company_id']] for x in roles]

    for i in range(10):
        res.append({"role":roles[i], "company":rel_comps[i]})

    return {'response': res}