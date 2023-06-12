#!/usr/bin/python3
"""
https://replit.com/@JaneNgethe/Day2PythonBasicsAssignment#main.py
"""

# 2. Values
age = 49
points = 89.6
mean = 75
lang = "Python"
status = True
print("******Values******")
print("I am {} years old, love {} and attained {} points".format(
  age, lang, points))

# Types
print("******Types******")
print(type(age))
print(type(age) and type(mean))
print(type(points))
print(type(lang))
print(type(status))

# 3. Arithmetic Operations
x = 65
y = 32.4
z = 6
large = 1234567890
print("******Arithmetic Operations******")
print(x + y + z)
print(x - y)
print(y * z)
print(x / z)
print(x % z)
print("{:.1e}".format(x))
print("{:.2e}".format(y))
print("{:.1e}".format(large))
print("{:.4e}".format(large))
print("{:.15e}".format(large))

# 4 Comparison Operators
x = 5
y = 10
z = 15
print("******Comparison Operations******")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)

# Logical Operators
print("******Logical Operations******")
print(z > y and y > x)
print(y > x or y > z)
print(not (x > z))

# 5 Basic Calculations
print("******Basic Calculations******")
num1 = int(input("Key in First Number: "))
num2 = float(input("Key in Second Number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
