# create tuple with number from 1 to 10
number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(number)

# print the first and last numbers
print(number[0])
print(number[9])

# check if the number 5 is in the tuple
if 5 in number:
    print("yes in the tuple") 
else:
    print("not in the tuple")

# find the sum of the all numbers
total = sum(number)
print(total)

# find the max and min numbers in the tuple
maximum = max(number)
print(maximum)
minimum = min(number)
print(minimum)

# create the tuple with even number
for number in number:
    if number % 2 == 0:
        print(number)

# count how many times the number 2 appears in the tuple
num = (1, 2, 2, 3, 4, 2, 5)
count = 0 
for num in num:
    if num == 2:
        count += 1
        print(count)

# reverse the tuple using slicing
num = (1, 2, 3, 4, 5)
reversed_tuple = num[::-1]
print(reversed_tuple)

# create two tuples and joing them together 
num1 = (1, 2, 3, 4, 5)
num2 = (6, 7, 8, 9, 10)
add = num1 + num2
print(add)

# use a loop to print only the numbers greater than 5 in a tuple
num3 = (5, 10, 15, 20, 40)
found = False
for num in num3:
    if num > 5:
        found = True
        print(num)
if not found :
        print("No numbers found greater than 5 in the tuple.")    

        


    



