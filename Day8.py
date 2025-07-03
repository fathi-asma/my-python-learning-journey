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



                      




    




    



  

