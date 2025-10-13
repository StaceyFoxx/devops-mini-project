"""
SQL-Connector and all things DB go in here
"""
import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx


# EXAMPLE 1
def get_all_characters_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM students"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_new_character_db(new_student_dict):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        print("ADD THIS STUDENT TO DB:", new_student_dict)

        query = f"""
         INSERT INTO students (name, class, IQ, house, quidditch)
         VALUES ('{new_student_dict['name']}', '{new_student_dict['class']}', {new_student_dict['IQ']}, {new_student_dict['house']}, {new_student_dict['quidditch']})
         """

        # Execute the query
        cur.execute(query)

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        print("Student added successfully!")

        query = """SELECT * FROM students"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def delete_student_by_id(id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        del_query = """DELETE FROM students WHERE student_id = {}""".format(id)
        cur.execute(del_query)

        db_connection.commit()  # IMPORTANT!!! Commit the transaction to apply the deletion

        # you can leave little messages for yourself and debugging like this
        print(f"Record with student_id {id} deleted successfully.")

        # NOTE - I've added this so I can return the remaining students back to my API
        # I don't need to do this but this is something that I've decided my app does
        select_query = "SELECT * FROM students"
        cur.execute(select_query)
        remaining_records = cur.fetchall()  # Get all remaining records
        cur.close()

        return remaining_records


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    print("TESTING DB CONNECTION")
    print(get_all_characters_db())
