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


    




    



  

