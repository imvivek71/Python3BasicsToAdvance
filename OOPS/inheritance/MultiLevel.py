#  Multi level inheritance


class Super:
    def add(a,b):
        sum = a+b
        return sum


class SubSuper(Super):
    def sub(a,b):
        return a-b


class Child(SubSuper):
    def mul(a,b):
        return a*b



print(Child.add(1,2), Child.sub(9,1))

