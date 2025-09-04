import mysql.connector
import logging
import functools
import re

logging.basicConfig(filename="student_records.log",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG,
                    filemode="a+")

logger=logging.getLogger()

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb",
       auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS Students (id INT primary key, name VARCHAR(50), email VARCHAR(50), phone VARCHAR(50), city VARCHAR(50), course VARCHAR(50))")

shared={}

def transactions_decorator(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
              try:
                     func(*args,**kwargs)
                     logger.debug(f"Transaction performed on function {func.__name__}()")
              except ValueError as e:
                     logger.error(f"Some error occured at function {func.__name__}")
                     return e
       return wrapper

def validation_decorator(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
              regex = regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
              email = shared.get("email")
              
              if(re.fullmatch(regex, email)):
                     print(email)
                     func(*args, **kwargs)
                     print("Valid Email")
              else:
                     raise ValueError('Invalid email')
              # func(*args, **kwargs)
       return wrapper

@transactions_decorator
@validation_decorator
def insert_values():
       try:
              id = int(input("Enter Integer Student ID: "))
              name = input("Enter Name: ")
              email = input("Enter Email: ")
              phone = input("Enter Phone Number: ")
              city = input("Enter City: ")
              course_information = input("Enter Course Information: ")
              shared["email"]=email
              cursor.execute(f"insert into students values ('{id}','{name}','{email}','{phone}','{city}','{course_information}')")
              conn.commit()
              return 'Values Inserted Successfully'
       except ValueError as e:
              print("Invalid Input, ", e)

@transactions_decorator
def select_values():
       cursor.execute(f"select * from students")
       rows = (cursor.fetchall())
       print('---------Student Details---------')
       for row in rows:
              print("ID:",row[0], "Name:",row[1], "Email:",row[2], "Phone:",row[3], "City:",row[4], "Course Information:",row[5])

@transactions_decorator
@validation_decorator
def update_values():
       try:
              updates = []
              values = []
              id = int(input("Enter Integer Student ID for which salary you want to update: "))
              name = input("Enter Name(if you do not want to update then enter None): ")
              email = input("Enter Email(if you do not want to update then enter None): ")
              phone = input("Enter Phone Number(if you do not want to update then enter None): ")
              city = input("Enter City(if you do not want to update then enter None): ")
              course = input("Enter updated course information(if you do not want to update then enter None): ")
              
              if name:
                     updates.append("name= %s")
                     values.append(name)
              if email:
                     updates.append("email= %s")
                     values.append(email)
              if phone:
                     updates.append("phone= %s")
                     values.append(phone)
              if city:
                     updates.append("city= %s")
                     values.append(city)
              if course:
                     updates.append("course= %s")
                     values.append(course)
              if not updates:
                     raise ValueError("No Values to input")
              query = f"update students set {', '.join(updates)} where id = {id}"
              cursor.execute(query, values)
              conn.commit()
              shared["email"]=email
              return 'Values Updated Successfully'
       except ValueError as e:
              print("Invalid Input: ", e)

@transactions_decorator
def delete_values():
       try:
              id = int(input('Enter the id of student you want to delete: '))
              cursor.execute(f"delete from students where id = {id}")
              conn.commit()
              print('Employee Deleted Successfully')
       except ValueError as e:
              print("Invalid Input, ", e)

while(True):
       try:
              print("---------Student Management System---------")
              print('1. Create New Students')
              print('2. Read All Students')
              print('3. Update Course Information')
              print('4. Delete Student')
              print('5. Exit')

              choice = int(input('Enter Your Choice: '))

              match choice:
                     case 1:
                            print(insert_values())
                     case 2:
                            select_values()
                     case 3:
                            update_values()
                     case 4:
                            delete_values()
                     case 5:
                            break
                     case default:
                            print('Invalid Choice')
       except ValueError as e:
              print("Invalid Input, ", e)