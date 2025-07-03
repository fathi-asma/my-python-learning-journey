# Write a funtion that prints "Hello world!"
def greet():
    print("Hello world!")
greet()

# write a function that takes user name as input and print greeting 
def greet_user(user):
      print("Hello!", user)
greet_user(input("Enter the name: "))    


# create a function that takes two numbers and prints their sum
def display_sumation(number1,number2):
     sum = (int(number1)+ int(number2))
     print("sumation is: ", sum)
display_sumation(input("Enter number 1: "), (input("Enter number two: ")))


# Create a function that takes a number and returns its square.
def square(num):
     result = int(num) * int(num)
     print("Square is:" , result)
square(input("Enter the number: "))   

# Write a function to check if a number is even or odd.
def check_even_or_odd(num):
     if int(num) % 2 == 0 :
          print("even")
     else :
          print("odd")
check_even_or_odd(input("Enter the number: "))

# Write a function that takes a list of numbers and returns the total sum.
def print_number(num):
     num_list = [int(x) for x in num.split()]
     total = sum(num_list)
     print(total)
print_number(input("Enter numbers: "))  

# Create a function that returns the largest number from three inputs.
def find_largest_number(num1,num2,num3):
     largest_number = max(int(num1),int(num2),int(num3))
     print("largest number is: ", largest_number)
find_largest_number(input("Enter the first number: "), input("Enter the second number: "),input("Enter the third number: "))  

# Write a function that takes a string and returns the number of vowels in it
def count_vowels(word):
     vowels = "aeiouAEIOU"
     count = 0
     for char in word:
          if char in vowels:
               count += 1
               return count
            
# three line mode
result1 = input("Enter the word: ")
find = count_vowels(result1)       
print("Number of vowels: ", find)

# two line mode
result2 = input("Enter the word: ")
print("Number of vowels: ", count_vowels(result2))

# one line mode
result3 = input("Enter the word: ", count_vowels(input("Enter the word: ")))


# Write a function that prints numbers from 1 to 10 using a loop.
def print_numbers():
     for i in range(1,11):
          print(i)
print_numbers()   

# Function to check if a number is a prime number
def is_prime(num):
     if num <= 1:
          return False
     for i in range (2, num):
          if num % i == 0:
               return False
     return True

number = int(input("Enter a number: "))
if is_prime(number):
     print(number, "is a prime number")
else :
      print(number, "is not a prime number")     



     
          
               

     

        