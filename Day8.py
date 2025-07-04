# Question1
# Calculator with Conditions.
def get_numbers():
   num1 = int(input("Enter the first number: "))
   num2 = int(input("Enter the second number: "))
   return num1 , num2

# Asks the user to choose an operation: add, subtract, multiply, divide.
def get_operation():
    operation = input("Enter the operation: ")
    return operation
   
#  Uses if-else to perform the operation and print the results 
def calculation():
    num1, num2 = get_numbers()
    operation = get_operation()

    if(operation == "Addition" or operation == "addition"):
        total = num1 + num2
    elif(operation == "Subtracts" or operation == "subtracts"):
        total = num1 - num2 
    elif(operation == "Multiply" or operation == "multiply"):
        total = num1 * num2 
    elif(operation == "Divide" or operation == "divide"):
        if num2 != 0:
            total = num1 / num2
        else :
            print("cant not divide by zero.")
            return 
    else :
        print("Invalid operation.")

    print ("Result: " , total)
calculation()    


# Question 2 
# Get user input for age.
def get_age():
    age = (int(input("Enter your age: ")))
    return age

# Use if-elif-else to classify
def Age_group_checker():
    age = get_age()

    if(age < 13):
        print("child.")
    elif(13 <= age < 20):
        print("Teen")
    elif(20 <= age < 60):
        print("Adult") 
    elif(age >= 60):
        print("senior") 
    else :
        print("Invalid age.")
Age_group_checker()  

# Question 3  
def shopping_list():
    items = ("bag", "shoes", "bottles", "back covers", "toys")
    return items

# Ask the user to enter an item name.
def item_name():
    item = input("Enter the item: ")
    return item

# use a condition to check if it's in the list.
def check_Available_notAvailable():
    items = shopping_list()
    item = item_name()

    if item in items:
        print("Available.")
    else :
        print("Not Availble.")    
check_Available_notAvailable() 

# Question 4

# Create a tuple of 5 fruits.
fruits = ("Apple", "Banana", "kiwi", "orange", "grapes")

# Print the first and last fruit using index.
print(fruits[0])
print(fruits[4])

# Use a function that accepts the tuple and prints items one by one using a loop.
def print_fruits(fruits_tuple):
    print("All the fruits in tuple: ")
    for fruit in fruits_tuple:
        print(fruit)
print_fruits(fruits)  


# Question 5

# Ask the user to enter a number.
number = int(input("Enter the number: "))

# Create a function check_even(num) that returns whether the number is even or odd.
def check_even(number) :
    if (number % 2 == 0):
        print("number is even")
    else :
        print("number is odd.")    
check_even(number)


# Question 6

# Ask the user to input marks for 3 subject
subject1_mark = int(input("Enter the first subject marks: "))
subject2_mark = int(input("Enter the second subject marks: "))
subject3_mark = int(input("Enter the third subject marks: "))

# Store in a list.
three_subject_marks = [subject1_mark, subject2_mark, subject3_mark]

# Calculate total function.
def total_marks():
    total = sum(three_subject_marks)
    print("Total marks: ", total)
    return total

#  Calculate average 
def average_marks():
    total = total_marks()
    average = total/3.0
    print("Average marks: " , average)
    return average

# Use if to check if the average is above 50 → "Pass", else "Fail".
average = average_marks()
if average > 50 :
    print("Pass.")
else :
    print("Fail.")   

# Task: Student Report Generator.
# Takes input for a student's name.
student_name = input("Enter the student name: ")

# Asks for marks in 3 subjects (Math, Science, English).
mark_Math = int(input("Enter the mark for maths subject: "))
mark_science = int(input("Enter the mark for science subject: "))
mark_english = int(input("Enter the mark for english subject: "))

#  Stores the marks in a list.
marks = [mark_Math, mark_science, mark_english]

# Calculates total and average using functions.
def total_marks():
    total = sum(marks)
    print("The total of the mark is: ", total)
    return total

def marks_average(total):
    average = total/3.0
    print("Average of the mark is: ", average)
    return average

def check_pass_fail(average):
    if average > 50 :
        return ("pass")
    else :
        return ("Fail") 

def grade(average):
    if average > 75 :
       return ("A")
    elif average > 60 or average < 74 :
        return ("B")
    elif average > 50 or average < 59 :
        return ("C")
    elif average < 50 :
        return ("F")
    else :
        return ("Invalide garde.") 
    
total = total_marks()
average = marks_average(total)
result = check_pass_fail(average)
grade_result = grade(average)

print("\n------ Student Report ------")
print("Student Name:", student_name)
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Result:", result)
print("Grade:", grade_result)    
                














                      




    




    



  

