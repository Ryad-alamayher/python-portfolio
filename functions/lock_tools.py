#lock_tools.py


def is_locked(failed, max_tries=3):
    """Return True if failed tries reach max_tries or more, else False."""
    return failed >= max_tries

def tries_left(failed, max_tries=3):
    """Return 0 if the account is locked, else max_tries - failed."""
    if(is_locked(failed , max_tries) == True):
        return 0
    else:
        return (max_tries - failed)
    
def status(failed):
    """Return account status as locked or active with remaining tries."""
    if(tries_left (failed) == 0):
        return "locked"
    else:
        return f"active ({tries_left(failed , max_tries = 3)} tries left)"
    


print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))