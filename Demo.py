import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="snow9823", host="localhost", port="5432")

cur = conn.cursor()
cur.execute('''CREATE TABLE student(NAME TEXT, AGE TEXT, ADDRESS TEXT)''')

print('connection success')
