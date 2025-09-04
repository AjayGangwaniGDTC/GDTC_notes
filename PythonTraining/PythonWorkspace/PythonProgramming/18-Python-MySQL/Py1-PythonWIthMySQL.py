import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb"
)

print("Connected to MySQL")
conn.close()