#####################################

# In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python,
# we can actually change the behavior of code at run-time.


class Monkey:
    def hey(self):
        print('This is monkey function')
def mnky(self):
    print('Monkey Patching is happening')


Monkey.hey = mnky
obj = Monkey()
obj.hey()


