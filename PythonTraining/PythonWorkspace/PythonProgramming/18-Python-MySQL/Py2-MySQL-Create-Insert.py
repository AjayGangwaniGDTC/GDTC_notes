import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb"
)

cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INT, name VARCHAR(20))")

# Insert data
cursor.execute("INSERT INTO students(id, name) VALUES(1,'Alice')")
cursor.execute("INSERT INTO students(id, name) VALUES(2,'Bob')")

conn.commit() # Save changes
print("Table created and inserted data")
cursor.close()
conn.close()
