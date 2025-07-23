try:
# Ask the user to input two numbers
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    total = first_number / second_number
    print("The total is: ", total)

except:
    print("Cant divide by 0.")
