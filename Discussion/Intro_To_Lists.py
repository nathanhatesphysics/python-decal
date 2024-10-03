# Indroduction to Lists
# Examples of Lists
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
planets = ["Mercury", "Earth", "Mars"]
mixed = [4, "Python", True, 3.14]
nested = [[1, 2, 3], [7, 4, 2], [8, 3, 6]]
empty = []

print(nested)

# Python is special, it remembers the position and value of every element in the list

# Adding elements at the end of a list with .append()
nums.append(11)
print(nums)

# Adding elements at a specific index can be done with .insert()

planets.insert(1, "Venus") # Places at that specific index and moves everything over 1
print(planets)

# Modification at a specific index
nums[1] = 222
print(nums)

# Delete from list with .remove()
# Delete from list with .pop()

planets.remove("Mercury") # Remove is used for looking for exact value, deletes first iteration of the value
print(planets)

planets.pop(1) # Pop removes a specific index
print(planets)

# Introduction to dictionaries
# Example dictionary

fourth_planet = {
    "name" : "Mars",
    "moons" : ["Phobos", "Deimos"],
    "diameter_km" : 6337,
    "atmosphere" : False
}

print(fourth_planet)
print(fourth_planet["name"])
print(fourth_planet.get("moons"))

# Modifying a dictionary
fourth_planet["atmosphere"] = True

print(fourth_planet)

# Adding an element to a dictionary
fourth_planet["color"] = "red"
print(fourth_planet)

# Removes an element from a dictionary
fourth_planet.pop("color")
print(fourth_planet)

# OR

del fourth_planet["moons"]
print(fourth_planet)

# Advanced
# Concatenating

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 
list4 = list2 + list1 # order matters

print(list1)
print(list2)
print(list3)
print(list4)

# .append nests lists

list1.append(list2)
print(list1)

# Slicing

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:5]) # same rules for counting apply

# Striding
# [start:stop:step]

stride_nums = numbers[::2]
print(stride_nums)

reverse_nums = numbers[::-1]
print(reverse_nums)

funky_nums = numbers[2:6:2]
print(funky_nums)

# Enumerating: Takes both index number and index value
for index, value in enumerate(mixed): # index, value could be anything
    print(index, value)

unsorted_list = [3, 1, 4, 5, 9]
unsorted_list.sort()
print(unsorted_list)

# Example 1
desserts = ["cookie", "ice cream", "brownie", "candy"]
c_words = []
for i in desserts:
    if i[0] == "c":
        c_words.append(i)
print(c_words)

words_c = [i.upper() for i in desserts if i[0] == "c"]
print(words_c)

# Example 2
fav_nums = {
    "alice" : [5, 101, 66],
    "bob" : [7, 23, 111],
    "chuck" : [26, 82, 84]
}

average_nums = []
for name, numbers in fav_nums.items(): #????
    average = sum(numbers)/len(numbers)
    average_nums.append(average)
print(average_nums)