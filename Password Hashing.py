import bcrypt

password = b"this is my password"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

entered_password = input("Enter password to login: ")
entered_password = bytes(entered_password, encoding='utf-8')

bcrypt.checkpw(entered_password)
