import psycopg2


def create():
    conn = psycopg2.connect(dbname="postgres!", user="postgres", password="snow9823", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')
    print('table created')
    conn.commit()
    conn.close()


def insert_data():
    conn = psycopg2.connect(dbname="postgres!", user="postgres", password="snow9823", host="localhost", port="5432")
    cur = conn.cursor()
    name = input('Enter name: ')
    age = input('Enter age: ')
    address = input('Enter address')

    print('table created')
    conn.commit()
    conn.close()


insert_data()
