# fix_the_functions.py


def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


# runtime: Calling print_header() before defining it causes NameError
print_header()


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        # semantic: Must return total minutes (failed * minutes) instead of returning 0
        return failed * minutes
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# runtime: Fixed keyword argument name from 'user' to 'username' to prevent TypeError
print(login_line(username="sara", failed=4))

# semantic: Added print() call so the generated status string is actually printed to terminal
print(login_line("omar", 1))