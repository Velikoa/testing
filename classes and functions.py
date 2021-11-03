number_1 = 5

number_2 = 4

def addition():
    number_1 + number_2
    print number_1 + number_2

print addition()





# Classes:

# Why put the "def __init__" phrase in a class?
# The init basically always runs the stuff that is below it. Think of it when starting a pc and want
# certain info total always work on startup - like your mouse etc.

# In the calcultor class below tehre is no __init__ so it does not have code that will always run when the class is called.



class calculator:             # Dont need parenthese when creating a class. If you have parentheses they
                            # simply show you where this class inherits some of its information.


    
    def addition(self, x, y):
        sum = x + y
        print sum

    def subtraction(self, x, y):
        sub = x - y
        print sub

    def multiplication(self, x, y):
        mult = x * y
        print mult

    def division(self, x, y):
        div = x / y
        print div

# NB!!! Why are you doing this? You need to call upon or RUN the "calcultor" program/class in order
# to have access to the functions within it. You cant use the functions if you havent started running
# the class to begin with - you need to refer to the class instance first!

calc_instance = calculator()

calc_instance.addition(5, 4)
calc_instance.multiplication(5, 4)


def FirstFactorial(num):
    factorial = 1

    for i in range(1, num + 1):
        # multiply each number between 1 and num
        # factorial = 1 * 1 = 1
        # factorial = 1 * 2 = 2
        # factorial = 2 * 3 = 6
        # factorial = 6 * 4 = 24
        # ...
        factorial = factorial * i

    return factorial


print FirstFactorial(4)