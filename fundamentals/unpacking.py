# =========================
# UNPACKING
# =========================

# BASIC UNPACKING 
user = ["Chloe", 33]
name, age = user
print(name, age)

order = ["Latte", 4.5]
item, price = order
print(item, price)


# UNPACKING WITH SPLIT (email)
email = "chloe@gmail.com"
username, domain = email.split("@")
print(username, domain)


# SWAPPING VALUES
x = 10
y = 20

x, y = y, x
print(x, y)  # 20 10