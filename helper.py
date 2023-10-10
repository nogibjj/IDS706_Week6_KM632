import mysql.connector
from faker import Faker

fake = Faker()
Faker.seed(4321)


def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="passw0rd"
    )
    conn.cursor().execute("CREATE DATABASE IF NOT EXISTS complexsql")
    conn.commit()
    return conn

def get_data_1():
    names = []
    for _ in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        names.append((first_name, last_name))
    return names

def get_data_2():
    data = []
    for _ in range(100):
        email = fake.email()
        address = fake.address()
        data.append((email, address))
    return data



def create_table_1(conn):
    with conn.cursor() as cursor:
        cursor.execute("USE complexsql")
        create_table_sql = """
        CREATE TABLE people (
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstname VARCHAR(255),
            lastname VARCHAR(255)  
        )
        """
        cursor.execute(create_table_sql)
        names = get_data_1()
        insert_query = "INSERT INTO people (firstname, lastname) VALUES (%s, %s)"
        for name in names:
            cursor.execute(insert_query, name)
    conn.commit()

def create_table_2(conn):
    with conn.cursor() as cursor:
        cursor.execute("USE complexsql")
        create_table_sql = """
        CREATE TABLE contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            emails TEXT,
            FOREIGN KEY (customer_id) REFERENCES people(id)
        )
        """
        cursor.execute(create_table_sql)
        for _ in range(100):
            email = fake.email()
            cursor.execute("SELECT id FROM people ORDER BY RAND() LIMIT 1")
            result = cursor.fetchone()
            customer_id = result[0] if result else None
            insert_query = "INSERT INTO contacts (customer_id, emails) VALUES (%s, %s)"
            cursor.execute(insert_query, (customer_id, email))
    conn.commit()

def create_table_3(conn):
    with conn.cursor() as cursor:
        cursor.execute("USE complexsql")
        create_table_sql = """
        CREATE TABLE addresses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            addresses TEXT,
            FOREIGN KEY (customer_id) REFERENCES people(id)
        )
        """
        cursor.execute(create_table_sql)
        for _ in range(100):
            address = fake.address()
            cursor.execute("SELECT id FROM people ORDER BY RAND() LIMIT 1")
            result = cursor.fetchone()
            customer_id = result[0] if result else None
            insert_query = "INSERT INTO addresses (customer_id, addresses) VALUES (%s, %s)"
            cursor.execute(insert_query, (customer_id, address))
    conn.commit()




def drop_table_1(conn):
    with conn.cursor() as cursor:
        cursor.execute("USE complexsql")
        drop_table_sql = "DROP TABLE IF EXISTS contacts"
        cursor.execute(drop_table_sql)
    conn.commit()

def drop_table_2(conn):
    with conn.cursor() as cursor:
        cursor.execute("USE complexsql")
        drop_table_sql = "DROP TABLE IF EXISTS people"
        cursor.execute(drop_table_sql)
    conn.commit()

def drop_table_3(conn):
    with conn.cursor() as cursor:
        cursor.execute("USE complexsql")
        drop_table_sql = "DROP TABLE IF EXISTS addresses"
        cursor.execute(drop_table_sql)
    conn.commit()



def create_tables(conn):
    drop_table_1(conn)
    drop_table_3(conn)
    drop_table_2(conn)
    create_table_1(conn)
    create_table_2(conn)
    create_table_3(conn)

    pass

