"""
def create_user(username, password, email,
                first_name=None, last_name=None, location=None):
    return {
        'username': username,
        'password': password,
        'email': email
    }
    
"""

def create_user(**kwargs):
    if 'username' not in kwargs:
        raise ValueError("Username is required")
    user = {}
    for name, value in kwargs.items():
        user[name] = value
    return user

user = create_user(password=123, email="john@gmail.com")
print(user)

