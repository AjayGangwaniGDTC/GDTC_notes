import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb"
)

cursor = conn.cursor()

# Function to fetch all the students
def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n----Student Records----")
    for row in rows:
        print("ID:", row[0], "Name:", row[1])
    print("--------------------------")

def update_student_name(student_id, new_name):
    query = "UPDATE students SET name = %s WHERE student_id = %s"
    values = (new_name, student_id)
    cursor.execute(query, values)
    conn.commit()
    print("\n Student ID:", {student_id}, "and updated name:", {new_name})

fetch_students()
update_student_name(1, "John")
cursor.close()
conn.close()