#!/usr/bin/python3
"""
https://replit.com/@JaneNgethe/Day3ControlFlowLoopsAssignment#main.py
"""

#2: C0nditional Statement- "if"
print("Conditional Statement- 'if'")
num = int(input("Please enter a number: "))
if num > 0:
  print(num, " is a Positive Number")
elif num < 0:
  print(num, " is a Negative Number")
else:
  print(num, " is Zero")

# 3. For Loop
print("For Loop")
for i in range(1, 11):
  print("The Square of ", i, "is ", i**2)

# 4. While Loop
print("While Loop")
num = int(input("Please enter a number to get its factorial: "))
i = 1
while num > 0:
  i *= num
  num -= 1
print("The Factorial is ", i)

# 5. Loop Control
print("Loop Control with For Loop")
for i in range(1, 21):
  if i % 2 == 1:
    print(i)
    continue
  if i >= 15:
    break
