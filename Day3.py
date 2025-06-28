# To check Enter numbers are equal or not
num1 = input ("Enter the number: ")
num2 = input ("Enter the second number: ")

if (num1 == num2):
    print("enter two numbers are equal")
else :
    print("enter two numbers are not equal")

# To check enter number number positive or negative
num1 = int(input("Enter the number: "))
if (num1 < 0 ):
    print("Number is negative.")
else :
    print("Number is positive.")   

# Find the Largest of Three Numbers.
num1 = input ("Enter the number: ")
num2 = input ("Enter the second number: ")  
num3 = input ("Enter the third number: ")

print (max(num1,num2,num3))

# Check Age for Voting
age = input("Enter your age: ")
if (age > 18):
    print("you can vote")
else :
    print("You can not vote")    

# Simple Grade Checker  
marks = input("Enter the marks: ") 
if (marks >= 75):
    print("A")
elif (marks >= 60):
    print("B")
elif (marks >= 50):
    print("C")
else :
    print("F")        







