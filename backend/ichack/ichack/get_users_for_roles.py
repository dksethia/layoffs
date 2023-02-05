from .worker_filter import wor_filter
from .query import query_with_fetchall

def get_users_for_roles(role_id):
    print(role_id)

    role = query_with_fetchall(f"SELECT * FROM Roles WHERE role_id={role_id}")[0]
    users = query_with_fetchall(f"SELECT * FROM People")

    users = sorted(users, key=lambda x : -wor_filter(x['keywords_in_ps'], x['former_role'], x['person_id'] in role['list_people_interested_in_role'].split(';'), role['name']))
    users = users[:10]

    return {"response":users}