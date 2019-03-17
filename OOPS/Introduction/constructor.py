#  With parameter
class Name:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def display(self):
        print(self.name)
        print(self.city)


a = Name('ashu', 'mumbai')


a.display()

class Student:
    def __init__(self):
        self.a = 10
        self.b =20
    def display(self):
        print(self.a)
        print(self.b)
z = Student()
z.display()


class Animal:
    def xyz(self):
        name ='A'
        classs = 'b'
        print(name, classs)


x = Animal()
x.xyz()

