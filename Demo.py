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
    cur.execute('''INSERT INTO student(NAME, AGE, ADDRESS) VALUES ('John', '25', 'NY');''')
    print('table created')
    conn.commit()
    conn.close()


insert_data()
