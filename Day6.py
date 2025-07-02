# Write a funtion that prints "Hello world!"
def greet():
    print("Hello world!")
greet()

# write a function that takes user name as input and print greeting 
def name():
      print("Hello!", user)
name() 
user = input("Enter your name: ")

# create a function that takes two numbers and prints their sum
def num(num1,num2):
     sum = (int(num1)+ int(num2))
     print("sumation is: ", sum)
num(input("Enter number 1: "), (input("Enter number two: ")))


# Create a function that takes a number and returns its square.
def squ(num):
     result = int(num) * int(num)
     print("Square is:" , result)
squ(input("Enter the number: "))   

# Write a function to check if a number is even or odd.
def check(num):
     if int(num) % 2 == 0 :
          print("even")
     else :
          print("odd")
check(input("Enter the number: "))

# Write a function that takes a list of numbers and returns the total sum.
def print(num):
     num_list = [int(x) for x in num.split()]
     total = sum(num_list)
     print(total)
print(input("Enter numbers: "))  

# Create a function that returns the largest number from three inputs.
def largest(num1,num2,num3):
     largest_number = max(int(num1),int(num2),int(num3))
     print("largest number is: ", largest_number)
largest(input("Enter the first number: "), input("Enter the second number: "),input("Enter the third number: "))  

# Write a function that takes a string and returns the number of vowels in it
def vowels_find(word):
     vowels = "aeiouAEIOU"
     count = 0
     for char in word:
          if char in vowels:
               count += 1
               return count
            
# three line mode
result1 = input("Enter the word: ")
find = vowels_find(result1)       
print("Number of vowels: ", find)

# two line mode
result2 = input("Enter the word: ")
print("Number of vowels: ", vowels_find(result2))

# one line mode
result3 = input("Enter the word: ", vowels_find(input("Enter the word: ")))


# Write a function that prints numbers from 1 to 10 using a loop.
def number():
     for i in range(1,11):
          print(i)
number()   

# Function to check if a number is a prime number
def is_prime(num):
     if num <= 1:
          return False
     for i in range (2, num):
          if num % i == 0:
               return False
     return True

number = int(input("Enter a number: "))
if is_prime(num):
     print(number, "is a prime number")
else :
      print(number, "is not a prime number")     



     
          
               

     

        