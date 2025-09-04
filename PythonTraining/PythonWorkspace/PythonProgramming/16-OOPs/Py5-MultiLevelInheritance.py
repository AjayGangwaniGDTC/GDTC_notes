class Person:
    def __init__(s, name, age):
        s.name = name
        s.age = age
    def display(s):
        print('name: {}, age: {}'.format(s.name, s.age))

class Employee(Person):
    def __init__(s, id, name, age, salary):
        super().__init__(name, age)
        s.id = id
        s.salary = salary

    def display(s):
        super().display()
        print('id: {}, sub1: {}'.format(s.id, s.salary))

class Manager(Employee):
    def __init__(s, id, name, age,salary, team_size, project_name):
        super().__init__(id, name, age, salary)
        s.team_size = team_size
        s.project_name = project_name

    def display(s):
        super().display()
        print('team_size: {}, project_name: {}'.format(s.team_size, s.project_name))

man = Manager(10024, 'Alex', 33, 75000, 4, 'XYZ')
man.display()


