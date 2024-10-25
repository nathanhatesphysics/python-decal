list = [1, "one", 2, "two", 3, "three", 4, "four"]
my_dict = {}
for i in list:
    if type(i) == int:
        my_dict[i] = []
        for j in range(0, 4):
            my_dict[i].append(i ** j)
    else:
        my_dict[i] = [i] * 4
print(my_dict)

def check_prime(num):
    is_prime = True
    if num == 1:
        is_prime = False
        return((num, is_prime))
    elif num == 2:
        is_prime = False
        return((num, is_prime))
    elif type(num) == int:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        return((num, is_prime))
    else:
        return("Not an integer")

numbers_1_50 = []
for i in range(1, 51):
    numbers_1_50.append(i)

prime_numbers_1_50 = []
for i in numbers_1_50:
    prime_numbers_1_50.append(check_prime(i))

print(prime_numbers_1_50)