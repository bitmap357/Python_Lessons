import bcrypt

password = b"this is my password"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

