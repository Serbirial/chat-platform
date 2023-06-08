
def authenticated(given_auth_key: str, real_auth_key: str): # Helper tool to make sure a user is authenticated when doing things that need authentication.
    if real_auth_key == given_auth_key:
        return True
    else:
        return False
    


 
def has_shared_or_is_friend(db_conn): # You cannot get user info for a user you dont share something with, nor DM them.
    pass