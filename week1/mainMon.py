#!/usr/bin/python3
"""
https://replit.com/@JaneNgethe/Day5DataStructuresAssignment#main.py
"""

#List
my_list = [50, 51, 52, 53, 54, 55, 56, 57]
n_list = [55, 56, 50, 51, 52, 57, 53, 54]

#append()
my_list.append(58)
print("*****append(58)*****")
print(my_list)

#remove()
my_list.remove(50)
print("*****remove(50)*****")
print(my_list)

#sort()
n_list.sort()
print("*****sort()*****")
print(n_list)

#List comprehension
my_list = [1, 2, 3, 4, 5]
new_list = []
for i in my_list:
  square = i**2
  new_list.append(square)

print("*****List Comprehension- squares*****")
print(my_list)
print(new_list)

#Tuples
basket = ('apple', 'orange', 'apple', 'pear', 'orange', 'banana')
print("*****Tuple indexing*****")
print(basket[2])

print("*****count()*****")
print("Apple = ", basket.count("apple"))
print("Orange = ", basket.count("orange"))
print("Pear = ", basket.count("pear"))

#Dictionaries
person_ages = {
    "John": 25,
    "Alice": 32,
    "Bob": 41,
    "Emily": 19,
    "Michael": 56
}

#Add a new key-value
print("*****dict-Add new key-value*****")
person_ages["Joseph"] = 50
print(person_ages)

#Update the value of an existing key in the dictionary.
person_ages["Alice"] = 33
print("*****Update values in dict*****")
print(person_ages)

# Remove a key-value pair from the dictionary using the pop() method.
print("*****pop values in dict*****")
person_ages.pop("Alice")
print(person_ages)

#Sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 5, 8, 3, 10}
print("*****sets*****")
print(set1)
print(set2)

#Set Union()- Joins the 2 sets
print("*****Set union()*****")
print(set1.union(set2))

# intersection()- similar elements in both sets
print("*****Set intersection()*****")
print(set1.intersection(set2))

# difference()- returns elements that are present in set1 but absent in set2
print("*****Set difference()*****")
print(set1.difference(set2))
