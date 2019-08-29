# 
# Example file for variables
#

# Declare a variable and initialize it
a = 3
print(a)
# # re-declaring the variable works
a = 'prashant'
print(a)
# # ERROR: variables of different types cannot be combined
print(a + str(4))

# Global vs. local variables in functions
def fun1():
    
    global x
    x = 4
    print(x)
x = 5
print(x)

print(fun1())