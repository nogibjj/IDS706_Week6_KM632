import unittest
import mysql.connector

class TestDatabase(unittest.TestCase):
    def test_total_entries(self):
        # Database connection parameters
        config = {
            "host": "localhost",
            "user": "root",
            "password": "passw0rd",
            "database": "complexsql",  
        }

        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()

            cursor.execute("SELECT COUNT(*) FROM people;")
            people_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM contacts;")
            emails_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM addresses;")
            addresses_count = cursor.fetchone()[0]

        except mysql.connector.Error as error:
            print("Error:", error)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        total_entries = people_count + emails_count + addresses_count

        self.assertEqual(total_entries, 300)

if __name__ == "__main__":
    unittest.main()
