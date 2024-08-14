#!/usr/bin/env python3

print("===============================")

#Basic example of a for loop
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

print("===============================")

#Almost same example with a nested if
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    else:
        print(color)

print("===============================")

# For with tuples
point = (2.1, 3.2, 7.5)
for value in point:
    print(value)

#For with list of tuples
list_of_points = [(1,2), (2,3), (4,3)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")

print("===============================")

#For with dictionaries getting both values
ages = {'Kevin': 34, 'Bob': 21, 'Kayla': 26}
for key, value in ages.items():
    print(f"Person is {key}, and age is {value}.")

# For with dictionaries getting only the value
for value in ages.values():
    print(value)

#For with dictionaries getting only the key
for key in ages.keys(): #Or could be the default 'for key in ages:'
    print(key)

print("Dictionary items are converted into list of tuples with the items() method:")
print(ages.items())
print("Dictionary keys or values are converted into lists with the keys() or values() methods:")
print(ages.keys(), ages.values())
