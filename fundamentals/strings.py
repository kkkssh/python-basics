# =========================
# STRINGS
# =========================

# SPLIT
fruit_text = "apple banana grape"
fruit_list = fruit_text.split()
print(fruit_list)    # ['apple', 'banana', 'grape']


# SPLIT WITH SEPARATOR
fruit_text_with_commas = "apple,banana,grape"
fruit_list_from_commas = fruit_text_with_commas.split(",")
print(fruit_list_from_commas)    # ['apple', 'banana', 'grape']


# SPLIT WITH MAX SPLITS
domain = "mail.google.com"

full_split = domain.split(".")
print(full_split)  # ['mail', 'google', 'com']

limited_split = domain.split(".", 1)
print(limited_split)  # ['mail', 'google.com']


# EXTRACTING PART OF A STRING
email = "user@mail.google.com"

# Method 1: Using a variable
email_parts = email.split("@")
email_domain = email_parts[1]
print(email_domain)  # mail.google.com

# Method 2: Direct indexing
domain_direct = email.split("@")[1]
print(domain_direct)  # mail.google.com


# REPLACE (STRING UPDATE)
sentence = "Today's special is pasta"
updated_sentence = sentence.replace("pasta", "pizza")
print(updated_sentence)  # Today's special is pizza
print(sentence)      # Today's special is pasta

age_range_text = "twenty-five to thirty"
age_range_text = age_range_text.replace("thirty", "thirty-five")
print(age_range_text)    # twenty-five to thirty-five