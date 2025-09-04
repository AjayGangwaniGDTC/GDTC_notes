import psycopg2
from input import get_student_input
from validation import validate_student_data

# Connecting to an existing database
conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "admin123",
    host = "localhost",
    port="5432"
)

# Open cursor to execute database operations
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name VARCHAR(50), email VARCHAR(50), phone VARCHAR(50), city VARCHAR(50), course VARCHAR(50))")

def insert_student():
    data = get_student_input()
    is_valid, msg = validate_student_data(data)
    if not is_valid:
        print(f"Validation Failed: {msg}")
        return "Insertion aborted due to validation failure."
    try:
        cursor.execute("""
            INSERT INTO students (id, name, email, phone, city, course)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (int(data['id']), data['name'], data['email'], data['phone'], data['city'], data['course']))
        conn.commit()
        print("Student inserted successfully.")
        return "Inserted successfully."
    except psycopg2.errors.IntegrityError:
        return "Insertion failed: Duplicate ID or integrity error."
    except Exception as e:
        return f"Insertion failed: {e}"
    
def select_students():
    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        print("\n---------Student Records---------")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]} | Phone: {row[3]} | City: {row[4]} | Course: {row[5]}")
        return "Displayed all students."
    except Exception as e:
        return f"Error fetching records: {e}"
    
def update_student():
    try:
        sid = int(input("Enter Student ID to update: "))
        field = input("Enter field to update (name/email/phone/city/course): ").strip().lower()
        value = input("Enter new value: ").strip()

        if field not in ["name", "email", "phone", "city", "course"]:
            return "Invalid field selected."

        if field == "email":
            temp_data = {
                "id": "1", "name": "dummy", "email": value,
                "phone": "000", "city": "x", "course": "x"
            }
            is_valid, msg = validate_student_data(temp_data)
            if not is_valid:
                return f"Email validation failed: {msg}"

        query = f"UPDATE students SET {field} = %s WHERE id = %s"
        cursor.execute(query, (value, sid))
        conn.commit()

        if cursor.rowcount == 0:
            return "No record found with that ID."
        return "Record updated successfully."
    except ValueError:
        return "ID must be a number."
    except Exception as e:
        return f"Update failed: {e}"
    
def delete_student():
    try:
        sid = int(input("Enter Student ID to delete: "))
        cursor.execute("DELETE FROM students WHERE id = %s", (sid,))
        conn.commit()
        if cursor.rowcount == 0:
            return "No record found with that ID."
        return "Student deleted successfully."
    except ValueError:
        return "ID must be a number."
    except Exception as e:
        return f"Delete failed: {e}"
    
def main():
    print("Main Function")
    while True:
        print("\n---------Student Management System---------")
        print("1. Insert Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1: print(insert_student())
                case 2: print(select_students())
                case 3: print(update_student())
                case 4: print(delete_student())
                case 5: print("Exiting..."); break
                case _: print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
            
if __name__ == "__main__":
    main()
    
cursor.close()
conn.close()
