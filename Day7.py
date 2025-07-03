# Write a program that checks if a number entered by the user is positive.
def positive(num):
    if(num < 0 ):
        print("Number is negaive.")
    else :
        print("Number is positive.") 
positive(int(input("Enter the number: ")))

# Ask the user to enter their age. If the age is 18 or more, print a message saying they can vote.
def age(age):
    if(age >= 18) :
        print("you can vote.")
    else :
        print("You can not vote.")    
age(int(input("Enter your age: ")))    

# Get a number from the user. If the number is even, print "Even number".
def check(number):
    if(number % 2 == 0):
        print("Number is even.")
    else :
        print("Number is odd")    
check(int(input("Enter the number: ")))      

# Ask the user to enter two numbers. Print which one is greater.
def maximum(num1, num2):
    print(max(num1, num2)) 
maximum(int(input("Enter the first number: ")), int(input("Enter the second number: ")))

# Ask the user to enter a number. If the number is divisible by 3, print "Divisible by 3".
def divisible(number):
    if(number % 3 == 0):
        print("can divide by 3.")
    else :
        print("Cant divide by 3.")    
divisible(int(input("Enter the number: ")))   

# Write a program that checks if a given year is a leap year or not.
def check_leap_year(year):
    if(year % 400 == 0):
        print("leap year.")
    elif(year % 100 == 0):
        print("year is not leap.")
    elif(year % 4 == 0):
        print("year is leap.")
    else :
        print("year is not leap.")
check_leap_year(int(input("Enter the year: "))) 

#  Ask the user to enter a temperature. If it’s more than 30°C, print "It’s hot".
def temperature(temp):
    if(temp > 30) :
        print("its hot.")
    else :
        print("its not hot")
temperature(int(input("Enter the temperature: ")))  

# Get marks from the user. If the marks are above 50, print "Pass", otherwise print "Fail"
def marks_check(marks):
    if (marks > 50) :
        print("pass")
    else :
        print("Fail")
marks_check(int(input("Enter the marks: ")))

# Ask the user to enter a password. If the password is "admin123", print "Access granted".
def password(passw) :
    if (passw == "admin123") :
        print("Access granted")
    else :
        print("Access not granted.") 
password(input("Enter the password: "))  

#  Ask the user to input their gender ("M" or "F"). If "M", print "Hello Sir", if "F", print "Hello Ma'am".
def gender(gender):
    if (gender == "M"or gender == "m"):
        print("Hello sir.")
    elif (gender == "F" or gender == "f"):
        print("Hello maam") 
    else :
        print("please enter M or F. ")  
gender(input("Enter Gender M or F: "))                     
