# MINI PROJECT 1 - PASSWORD CHECKER

# Description:
# This program checks whether a password meets basic security requirements

# Requirements:
# - At least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one number
# - At least one special character

# Features:
# - Repeats until a valid password is entered
# - Provides specific feedback for missing conditions



while True:

    password = input("Create your password: ")

    has_upper = False
    has_lower = False
    has_num = False
    has_special = False

    for i in password:
        if "A" <= i <= "Z":
            has_upper = True
        elif "a" <= i <= "z":
            has_lower = True
        elif "0" <= i <= "9":
            has_num = True
        else:
            has_special = True


    if len(password) < 8:
        print("Password must include at least 8 characters")
    elif has_upper == False:    # elif not has_upper
        print("Add uppercase letter")
    elif has_lower == False:    # elif not has_lower
        print("Add lowercase letter")
    elif has_num == False:      # elif not has_num
        print("Add a number")
    elif has_special == False:  # elif not has_special
        print("Add a special character")
    else:
        print("Success!")
        break