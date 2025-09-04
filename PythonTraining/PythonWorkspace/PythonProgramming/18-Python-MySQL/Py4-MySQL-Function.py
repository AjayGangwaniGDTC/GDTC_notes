import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb"
)

cursor = conn.cursor()

def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n----Student Records----")
    for row in rows:
        print("ID:", row[0], "Name:", row[1])

fetch_students()
cursor.close()
conn.close()