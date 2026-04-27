# MINI PROJECT 3 - UNIQUE EMAIL FILTER

# Description:
# This program collects email addresses from the user,
# removes duplicates, and displays unique valid emails.

# Requirements:
# - Use sets to remove duplicates
# - Accept user input
# - Validate basic email format 

# Features:
# - Duplicate removal
# - Simple email validation
# - Displays total unique emails



def is_valid_email(email):
    if "@" not in email:
        return False
    
    if email.count("@") != 1:
        return False
    
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]       # username, domain = email.split("@")    
    
    if username == "" or domain == "":
        return False
    
    if "." not in domain:
        return False
    
    check_domain = domain.split(".", 1)
    domain_name = check_domain[0]
    domain_extension = check_domain[1]      # domain_name, domain_extension = domain.split(".", 1)

    if domain_name == "" or domain_extension == "":
        return False
    
    return True

emails = []

print("Enter email addresses (type 'exit' to finish): ")

while True:
    user_input = input("Email: ").strip()

    if user_input.lower() == "exit":
        break
    
    if is_valid_email(user_input):
        emails.append(user_input)
    else:
        print("Invalid email format. Please try again.")


unique_emails = set(emails)

print("Unique emails: ")
for email in unique_emails:
    print(email)

print(f"\nTotal unique emails: {len(unique_emails)}")