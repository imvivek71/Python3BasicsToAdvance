class TooYoungException(Exception):
    def __init__(self,x):
        self.msg=x
class TooOldException(Exception):
    def __int__(self,y):
        self.msg=y
age = int(input("Enter the age"))

if age>99:
    raise TooYoungException('You are overage')
elif age<18:
    raise TooOldException('You are underage')
else:
    print('You are perfect')
