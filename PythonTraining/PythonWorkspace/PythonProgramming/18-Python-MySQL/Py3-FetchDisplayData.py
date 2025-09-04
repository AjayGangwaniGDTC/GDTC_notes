import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()
for row in rows:
    print("ID:",row[0], "Name:",row[1])

cursor.close()
conn.close()