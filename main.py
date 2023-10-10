from helper import create_database, create_tables

def main():
    conn = create_database()
    create_tables(conn)


if __name__ == "__main__":
    main()
