from mylib.helper import create_database, create_tables, run_queries


def main():
    conn = create_database()
    create_tables(conn)
    run_queries(conn)
    conn.close()


if __name__ == "__main__":
    main()
