# Question 1

def computePower(x, y):
    number_initial = x
    number_current = 1
    for i in range(1, y + 1):
        number_current *= (number_initial)
    return (number_current)

print(computePower(4, 3))

# Question 2

def temperatureRange(temps):
    max_temp = temps[0]
    min_temp = temps[0]
    for i in temps:
        if i > max_temp:
            max_temp = i
    for i in temps:
        if i < min_temp:
            min_temp = i
    return (max_temp, min_temp)
print(temperatureRange([65, 43, 76, 34, 9]))

# Question 3

def isWeekend(x):
    weekday = True
    if (0 < x < 6):
        weekday = True
    else:
        weekday = False
    return (weekday)

print(isWeekend(4))
print(isWeekend(7))

# Question 4

def fuel_efficiency(distance, fuel):
    eff = distance/fuel
    return (round(eff, 2))

print(fuel_efficiency(70, 21.5))

# Question 5

def decodeNumbers(n):
    last_number = n % (n//10)
    cut_number = n//10
    cut_number_digits = 0
    while cut_number != 0:
        cut_number = cut_number//10
        cut_number_digits = cut_number_digits+1
    return (last_number * (10**cut_number_digits) + n//10)
print(decodeNumbers(56789))

# Question 6

# 6.1
def min_for_loop(numbers):
    min_number = numbers[0]
    for i in (numbers):
        if min_number > i:
            min_number = i
    return min_number
lst = [4, 3, 0, 2, 7, 1]
print(min_for_loop(lst))

# 6.2
def min_while_loop(numbers):
    min_number = numbers[0]
    n = 0
    while n < (len(numbers)):
        if min_number > numbers[n]:
            min_number = numbers[n]
        n += 1
    return min_number
print(min_while_loop(lst))

# Question 7
def vowels_and_consonants(text):
    vowels_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    vowels = 0
    consonants = 0
    vowels_list_checker = 0
    for x in text:
        if x.isalpha() == True:
            for y in vowels_list:
                if (x == y):
                    vowels += 1
                else:
                    vowels_list_checker += 1
            if vowels_list_checker == len(vowels_list):
                consonants += 1
        vowels_list_checker = 0
    return (vowels, consonants)
print(vowels_and_consonants("This is a sentence."))

# Question 8

def digital_root(num):
    final_number = 0
    for i in str(num):
        final_number += int(i)
    return final_number

print(digital_root(123))



