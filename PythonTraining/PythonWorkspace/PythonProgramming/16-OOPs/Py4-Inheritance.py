class Person:
    def __init__(s, name, age):
        s.name = name
        s.age = age
    def display(s):
        print('The name {} and age {}'.format(s.name, s.age))

class Student(Person):
    def __init__(s, id, name, age, sub1, sub2):
        Person.__init__(s, name, age)
        s.id = id
        s.sub1 = sub1
        s.sub2 = sub2
    def display(s):
        print('id {}, sub1 {}, sub2 {}'.format(s.id, s.sub1, s.sub2))

s1 = Student(1002,'Ramesh', 21, 70, 85)
s1.display()