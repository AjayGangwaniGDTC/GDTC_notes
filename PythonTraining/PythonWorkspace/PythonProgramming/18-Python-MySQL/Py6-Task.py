import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="godigitaldb"
)

cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS Employee (id INT primary key, name VARCHAR(50), age INT, salary FLOAT)")

def insert_values():
       id = int(input("Enter Integer Employee ID: "))
       name = input("Enter Name: ")
       age = int(input("Enter Age: "))
       salary = float(input("Enter Salary: "))
       cursor.execute(f"insert into employee values ('{id}','{name}','{age}','{salary}')")
       conn.commit()
       print('Values Inserted Successfully')

def select_values():
       cursor.execute(f"select * from employee")
       rows = (cursor.fetchall())
       print('---------Employee Details---------')
       for row in rows:
              print("ID:",row[0], "Name:",row[1], "Age:",row[2], "Salary:",row[3])


def update_values():
       id = int(input("Enter Integer Employee ID for which salary you want to update: "))
       salary = float(input("Enter updated salary: "))
       cursor.execute(f"update employee set salary = {salary} where id = {id}")
       conn.commit()
       print('Salary Updated Successfully')

def delete_values():
       id = int(input('Enter the id of employee you want to delete: '))
       cursor.execute(f"delete from employee where id = {id}")
       conn.commit()
       print('Employee Deleted Successfully')

while(True):
       print("---------Employee Management---------")
       print('1. Create New Employee')
       print('2. Read All Employees')
       print('3. Update Salary')
       print('4. Delete Employee')
       print('5. Exit')

       choice = int(input('Enter Your Choice: '))

       match choice:
              case 1:
                     insert_values()
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

cursor.close()
conn.close()


