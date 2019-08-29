#
# Example file for working with functions
#

# define a basic function

def hello():
    print('Hello World')
# function that takes arguments
def sum(a,b):
    sumn = a + b
    return sumn

# function that returns a value


# function with default value for an argument
def avg(b,a=2):
    avgn = (a+b)/2
    return avgn

#function with variable number of arguments
def sumall(*args):
    result = 0
    for i in args:
        result += i
    return result

print(sum(3,4))
print(avg(4))
print(avg(3,4))
print(sumall(2,3,4,5))
