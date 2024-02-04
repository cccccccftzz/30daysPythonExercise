"""
() are used for Methods 在method函数后用的.或者在method中限定一个局部的运算,通常意义中的()
[] are used For List/arrays 只有用来定义一个字串，或者读取一个字串中的某个位置的时候才会用到
{} are used to set scope 在一串字符中划定一个scope来进行methods运算，但如果已经在运算中的某一步的话只需要用()
"""

print("Exercise: Level 1")

print("a) 3^2=(3**2)")  # () cannot use for algorithm
print("b) 3^2=[3**2]")  # [] cannot use for algorithm either
print(
    f"c) 3^2={3**2}"
)  # Only {} inside the f-string is use for still carrying on the algorithm

# print(f"3^2={3**{1+2}}") CANNOT WORK, only can use () to set another scope inside {}
print(f"d) 3^2={3**(1+2)}")
print(f"d2) 3^2.5={3**(1+(0.5+1))}")

# print(f"3^2={3**[1+2]}") CANNOT WORK, cuz we dont hv any list

print(f"e) the remainder of 5÷2 is {5%2}")

print(f"f) 5÷2 and remove the remainder {5//2}")

print(f"g) 5÷2取整数 = {int(5/2)}")

# checking types of the data

# Number
print(type(10))
print(type(3.14))
print(type(5 + 6j))
print(
    type(5 + 6j + 3)
)  # only applicable to j!! by right shouldnt put any undefined vairables.

# Booleans
print(type(True))

# string
print(type("Fangting"))

# List [], Set{}, Turple(),
print(type([1, 2, 5]))  # List - ordered collection []
print(type([1, 2, "fangting"]))  # Can store difference data types

print(
    type({"1st sty", "Base floor", "5th sty", 6})
)  # set - unordered collection () 不懂->stores only unique items.

print(type(("Fangting", "lx", 5)))  # Tuple - ordered but cannot modified anymore

# Dictionary 用{:}
print(type({"Name": "Fangting"}))  # Dictionary - unordered & pair

print("Exercise: Level 3")
print(type(True), type([1, 2, 5]))
print(type(3), type(5.5), type(3 + 5j))
print(
    type(False),
    type(["fangting", "lx", "python"]),
    type(("fangting", "lx", "python")),
    type({1.5, 6.7, 4.4}),
    type({"name": "fangting"}),
)

print("Exercise: Level 3*")
# Exercise: Level 3* To find an euclidian distance between (2,3) and (10,8)
print(((8 - 3) ** 2 + (10 - 2) ** 2) ** 0.5)
print(f"The euclidian distance between (2,3) and (10,8) is {((8-3)**2+(10-2)**2)**0.5}")

print("Exercise: Level 3**")
# Exercise: Level 3** To find an euclidian distance between (X1,Y1) and (X2,Y2)
X1 = int(
    input("X1")
)  # No difference between "" and '' if inside a method to define a variation
Y1 = int(input("Y1"))
X2 = int(input("X2"))
Y2 = int(input("Y2"))
print(
    f"The euclidian distance between ({X1},{Y1}) and ({X2},{Y2}) is {((Y2-Y1)**2+(X2-X1)**2)**0.5}"
)
print(
    f"The euclidian distance between (X1,Y1) and (X2,Y2) is {((Y2-Y1)**2+(X2-X1)**2)**0.5}"
)  # 如果在字串里但是不加{}的变量是没有办法进行运算的
