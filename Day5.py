# create tuple with number from 1 to 10
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers)

# print the first and last numbers
print(numbers[0])
print(numbers[9])

# check if the number 5 is in the tuple
if 5 in numbers:
    print("yes in the tuple") 
else:
    print("not in the tuple")

# find the sum of the all numbers
total = sum(numbers)
print(total)

# find the max and min numbers in the tuple
maximum = max(numbers)
print(maximum)
minimum = min(numbers)
print(minimum)

# create the tuple with even number
for number in numbers:
    if number % 2 == 0:
        print(number)

# count how many times the number 2 appears in the tuple
nums = (1, 2, 2, 3, 4, 2, 5)
count = 0 
for num in nums:
    if num == 2:
        count += 1
        print(count)

# reverse the tuple using slicing
num = (1, 2, 3, 4, 5)
reversed_tuple = nums[::-1]
print(reversed_tuple)

# create two tuples and joing them together 
num1 = (1, 2, 3, 4, 5)
num2 = (6, 7, 8, 9, 10)
total = num1 + num2
print(total)

# use a loop to print only the numbers greater than 5 in a tuple
numbers = (5, 10, 15, 20, 40)
found = False
for num in numbers:
    if num > 5:
        found = True
        print(num)
if not found :
        print("No numbers found greater than 5 in the tuple.")    

        


    



