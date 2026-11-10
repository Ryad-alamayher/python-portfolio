#password_check.py




def long_enough(password, minimum=8):
    """return true if the password > or equal the minimum digit """
    if(len(password) >= minimum):
        return True
    else:
        return False

def differs_from_username(password, username):
    """return true if password and username not equal"""
    if(password != username):
        return True
    else:
        return False



def password_ok(password, username):
    """return the result of the functions"""
    if (long_enough(password , minimum=8) == True and differs_from_username(password , username) == True):
        return True
    else:
        return False
    
    

username = input("Username: ")
password = input("Password: ")

    
if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")

