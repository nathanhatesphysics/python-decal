import numpy as np

# Question 1

arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])

def odd_rows(input):
    filter = np.all(input % 2 != 0, axis=1)
    output = input[filter]
    return(output)

print(odd_rows(arr))

# Question 1 old work

def odd_rows2(input):
    output = np.array([[]])
    for i in range(0, len(input[:, 0])):
        counter = 0
        for j in input[i, :]:
            if j % 2 != 0:
                counter += 1
        if counter == len(input[i, :]):
            output = np.append(output, input[i, :], axis = 1)
    return(output)

# print(odd_rows2(arr))

# Question 2

# 2.1
long_arr = np.array([])
long_arr = np.repeat(0, 64, axis=0)
board1 = long_arr
board1.shape = (8, 8)
print(board1)

# 2.2
board2 = board1
for i in range(0, len(board2[:, 0]), 2):
    for j in range(0, len(board2[i, :]), 2):
        board2[i, j] = 1
print(board2)

# 2.3
board3 = board2
for i in range(1, len(board3[:, 0])+1, 2):
    for j in range(1, len(board3[i, :])+1, 2):
        board3[i, j] = 1
print(board3)

# 2.4
board3.shape = (1, 64)
board4 = np.delete(board3, 0)
board5 = np.append(board4, [0])
board5.shape = (8, 8)
print(board5)

# Question 3

universe = np.array(["galaxy", "clusters"])
def expansion(input, spaces):
    output = np.array([])
    for word in input:
        new_word = ""
        for char in word:
            new_word += char
            if str.isalpha(char) == True:
                new_word += " "*spaces
        output = np.append(output, new_word)
    return output
print(expansion(universe, 2))

# Question 4

planets = np.random.randint(100, 1000, (5, 5))
print(planets)
def second_largest(input):
    output = np.array([])
    for i in range(0, len(input[:, 0])):
        true_max = 1
        for num in (input[i, :]):
            if num != max(input[i, :]) and num > true_max:
                true_max = num
        output = np.append(output, true_max)
    return output
print(second_largest(planets))
            


