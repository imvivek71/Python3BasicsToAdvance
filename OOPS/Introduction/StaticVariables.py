class Number:
    a = 10
    def __init__(self):
        Number.b = 20
        print(Number.b)
    def ashu(self):
        Number.c = 30
        print(Number.c)
    @staticmethod
    def Sta():
        Number.d = 40
        print(Number.d)
    @classmethod

    def Cls(cls):
        cls.e = 100
        Number.x = 120
        print(cls.e, Number.x)


z = Number()
z.ashu()
z.Sta()
z.Cls()