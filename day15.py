#Python Type Errors

print("Practise all the errortype in showcase".center(80, "-"))

print("SyntaxError".center(80, "-"))
# print'Hello World' SyntaxError

print("NameError".center(80, "-"))
# print(age)
# Age is not defined

print("IndexError".center(80, "-"))
name = ['a','b','c']
# print(name[3])
# Dont hv index 3 in name list

print("ModuleNotFoundError".center(80, "-"))
# import maths
#ModuleNotFoundError: No module named 'maths'
import math #Correct module name then can work

print("AttributeError".center(80, "-"))
import math
# math.PI 
#AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi) #Can work

print("KeyError".center(80, "-"))
user = {
    'name' : 'Fang Ting',
    'age' : '30',
    'skills' : 'bodybuilding'
}
print(user['name'])
#print(user['Name']) 
#KeyError: 'Name'

print("TypeError".center(80, "-"))
'''
a = 4 + '3'
print(a)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

print("ValueError".center(80, "-"))
'''
output = int('12a')
print(output)
ValueError: invalid literal for int() with base 10: '12a'
'''

print("ImportError".center(80, "-"))
#from math import power
#ImportError: cannot import name 'power' from 'math' (unknown location)
from math import pow #Correct Power function name
output = pow(2,3)
print(output)

print("ZeroDivsionError".center(80, "-"))
'''
c = 1/0
print(c)
ZeroDivisionError: division by zero
'''

