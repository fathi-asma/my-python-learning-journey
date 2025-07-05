# Train Ticket Price Checker.

# Asks the user to enter their age
def get_age():
    age = int(input("Enter your age: "))
    return age

def check_status():
    status = input("Are you a student (yes/no): ")
    return status

def calculate_ticket_price():
    regular_price = 100

    if age < 12:
        discount = (regular_price * 50 ) / 100
    
    elif age >= 60:
        discount = (regular_price * 30) / 100

    elif status == "yes" :
        discount = (regular_price * 10) / 100

    else :
        discount = 0

    final_price = regular_price - discount
    return final_price    
    
age = get_age()
status = check_status()
final_price = calculate_ticket_price()

print("The age is : ", age)
print("The status is : ", status)
print("Final Ticket price: ", final_price)
    

        
        





    

