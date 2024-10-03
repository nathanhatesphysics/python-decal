# Loops do things over and over again
# Performs an action over each element of a list

# Ex
x = 10
while ( x > 0 ):
    print("action")
    print(x)
    x -= 1 # always change the conditional value at the end of the loop, performs operation on that value and not the one after it

# for loop ranges: creates a list of numbers for you

sum = 0
for i in range(1, 51): # range stop value disclusive, start value inclusive
    sum += i           # i = placeholder for each value in the list, could be anything

list_of_names = ["pranathi", "charlie", "mira", "katie", "brianna"]
line = ""
for name in (list_of_names):
    line += (name + " ")

print(line)
