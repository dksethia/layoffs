from .query import query_with_fetchall

def get_login_verification(email, password):
    print(email, password)
    print(f"SELECT * FROM People WHERE email={email}")
    user = query_with_fetchall(f"SELECT * FROM People WHERE email=\"{email}\"")
    print(user)
    if user is None:
        return False
    user = user[0]
    if user['password'] != password:
        return False
    
    return user