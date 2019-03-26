# Static Variables


class Number:
    a = 10

    def __init__(self):
        Number.a = 20
        print(Number.a)
        del Number.a

    def ashu(self):
        Number.a = 30
        print(Number.a)

    @staticmethod
    def Sta():
        Number.d = 40
        
        print(Number.d)

    @classmethod
    def Cls(cls):
        cls.e = 100
        Number.x = 120
        print(cls.e, Number.x)

    def displayall(self):
        print(Number.a,Number.a)


z = Number()
z.ashu()
z.Sta()
z.Cls()
z.displayall()
print('Delete ', z.a)

print(Number.__dict__)
del Number.a
print(Number.__dict__)
