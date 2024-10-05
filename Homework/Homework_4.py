# Problem 2
# 2.1
numbers_1_through_20 = []
for i in range(1, 21):
    numbers_1_through_20.append(i)
print(numbers_1_through_20)

"""
initially tried to use range function, 
but it output the literal range value instead of a list
"""

# 2.2
squared_numbers = numbers_1_through_20
def square_list(input_list):
    for i in (enumerate(input_list)):
        input_list[i[0]] = i[1] ** 2
    return input_list
squared_numbers = square_list(squared_numbers)
print(squared_numbers)

"""
originally function only worked because the list nicely increased by 1 due to me only using the index
had to use the enumerate of the input to generalize the function for any list

also had to look up what enumerate actually did, 
which is turn every element in the list into a tuple with the first value being it's index
"""

# 2.3
first_15 = squared_numbers
def first_15_list(input_list):
    output_list = input_list[0:15]
    return output_list
print(first_15_list(first_15))

# 2.4
every_5th = squared_numbers
def get_every_5th(input_list):
    output_list = input_list[::4]
    return output_list
print(get_every_5th(every_5th))

# 2.5
fancy_list = squared_numbers
def slice_and_stride(input_list):
    """
    >>> slice_and_stride([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])
    [225, 144, 81, 36, 9]
    """
    output_list = input_list[::-1][3:][::-1][2::3][::-1]
    return output_list
print(slice_and_stride(fancy_list))
"""
confused on what the question is asking? just sliced last 3 elements, then listed the 3rd elements in reverse order
"""

# Problem 3: 2D Lists
def create_2d_list():
    column = []
    for i in range(1, 26, 5):
        row = []
        for j in range(i, i+5):
            row.append(j)
        column.append(row)
    return column

matrix = create_2d_list()
print(matrix)

"""
append wasn't working because the row initialization was outside the for loop, now fixed
"""

# 3.2
def multiples_of_3(input_matrix):
    output_matrix = input_matrix
    for i in output_matrix:
        current_index = 0
        for j in i:
            if j % 3 == 0:
                i[current_index] = "?"
            current_index += 1
    return output_matrix
new_matrix = multiples_of_3(matrix)
print(new_matrix)

# 3.3
def sum_all_numbers(input_matrix):
    output_number = 0
    for i in input_matrix:
        current_index = 0
        for j in i:
            if j != "?":
                output_number += j
    return output_number
print(sum_all_numbers(new_matrix))


if __name__ == "__main__":
    import doctest
    doctest.testmod()