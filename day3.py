# Operator

print("Catch up in Preview".center(80, "-"))
first_name = "Fang Ting"
a = 1
a = a | 3
print(a)  # |,^,<<=,>>= for bit operation no need to learn first

print(len("milk") == len("talk"))
print(len("milk") < len("talk"))

print(False == 0)
print(True == 3)  # True == 1 ONLY
print(False == False)

print(f"{1 == 0}")
print(f"{1 != 0}")

print(f"{not not 0 = }")

print("Exercise 1-3".center(50, "-"))
age = 30
height = 163.5
a = height + 5j
print(f"{age,height,a}")
print(f"{age} {height} {a}")

print("Exercise 4".center(50, "-"))
base_of_triangle = int(input("base of the triangle"))
height_of_triangle = int(input("height of the triangle"))
area_of_triangle = 0.5 * base_of_triangle * height_of_triangle
print(area_of_triangle)

print("Exercise 5".center(50, "-"))
side_a = int(input("side a of the triangle"))
side_b = int(input("side b of the triangle"))
side_c = int(input("side c of the triangle"))
perimeter_of_triangle = side_a + side_b + side_c
print(perimeter_of_triangle)

print("Exercise 8".center(50, "-"))
# Given equation: y = 2x -2

slope = 2
x_intercept = 2 / slope
y_intercept = -2

print("Equation: y=2x-2,")
print(f"{slope = }")
print(f"{x_intercept = }")
print(f"{int(x_intercept) = }")
print(f"{y_intercept = }")

print("Exercise 9".center(50, "-"))
import math

point_one = (2, 2)
point_two = (6, 10)
slope_m = (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])
distance = math.sqrt(
    (point_two[1] - point_one[1]) ** 2 + (point_two[0] - point_one[0]) ** 2
)
print(f"{point_one = }")
print(f"{point_two = }")
print(f"{slope_m = }")
print(f"{distance = }")

print("Exercise 10".center(50, "-"))
compare_slope = slope_m > slope
print(
    f'The slope in task 9 {"is" if compare_slope else "is not"} bigger than the slope in task 8.'
)

print("Exercise 12".center(50, "-"))
length_one = len("python")
length_two = len("dragon")
print(
    f'The length of "python" {"is" if length_one > length_two else "is not"} longer than the one of "dragon"'
)
print(length_one > length_two)

print("Exercise 13".center(50, "-"))
print("on" in ["python"] and "on" in ["dragon"])
"""
Typical wrong mistake due to wrong type of the argument
when it is in [] meaning it will be one list 
'on' is not inside as it only one argument 'python' and 'dragon'
"""
print("on" in "python" and "on" in "dragon")
print(type(["python"]))
print(type("python"))
print("on" in ["python", "on"] and "on" in ["dragon", "on"])

print("Exercise 14".center(50, "-"))
print("on" in "I hope this course is not full of jargon.")

print("Exercise 15".center(50, "-"))
print("on" in ["python"] and "on" in ["dragon"])

print("Exercise 16".center(50, "-"))
length_python = len("python")
print(str(float(length_python)))

print("Exercise 17".center(50, "-"))
print("To juedge a even number")
number_three = int(input("To give a number to judge it is even number or odd number "))
# whether_number_three_even = bool (number_three % 2 == 0)  No need to assign bool() cuz already a bool type
whether_number_three_even = number_three % 2 == 0
print(
    f'The number {number_three} {"is" if whether_number_three_even is True else "is not"} is an even number '
)

print("Exercise 18".center(50, "-"))
print(7 // 3 == int(2.7))

print("Exercise 19".center(50, "-"))
print(type("10") == type(10))

print("Exercise 20".center(50, "-"))
print(int(float("9.8")) == 10)

print("Exercise 21".center(50, "-"))
working_hours = int(
    input("Enter Working Hours")
)  # Dont forget to convert the input to Int!!!
rate_per_hour = int(input("Enter rate per hour"))
pay_of_person = working_hours * rate_per_hour
print(f"Your weekly earning is = {pay_of_person}")

print("Exercise 22".center(50, "-"))
years_lived = int(
    input("Enter number of years you have lived")
)  # Dont forget to convert the input to Int!!!
seconds_of_life = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_of_life} seconds")

print("Exercise 23".center(50, "-"))
"""
aa = 1
power_a == 0
if (aa < 6):
    print ()
"""
# Display the table
for i in range(1, 6):
    print(f"{i} {1} {i} {i*i} {i*i*i}")
