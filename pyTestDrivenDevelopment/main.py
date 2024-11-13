# This just check sanitize but not used
import CheckAndClean

if __name__ == '__main__':
    cc = CheckAndClean.CheckAndClean("Database")

    # Let's try a common attack to show all user information
    print(cc.sanitize("'; SELECT * FROM Users; --"))


