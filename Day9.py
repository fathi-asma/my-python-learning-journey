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



#  Simple Shopping Bill Calculator
# Displays a list of 5 available items and their prices using a tuple
items = (("Bag", 1000), ("Shoes", 2500), ("Bottle", 500), ("Notebook", 300), ("Pen", 50))

# Asks the user to enter their name.
user_item = input("Enter your name: ")

# Asks the user how many different items they want to buy.
Number_of_items = int(input("Enter how many differnet items you want to buy: "))

# Ask user to enter item name
buy_item_name = input("Enter which item do you want to buy: ")

# Ask for the quantity
item_quantity = int(input("Enter the how much do want to buy: "))

# Check if the items exists in the tuple and calculate 
item_found = False

for item in items:
    if item[0] == buy_item_name:
        price = item[1]
        total = price * item_quantity
        print("Your total is: " , total)
        item_found = True
        break
if not item_found:
    print("Item not available.")   
   
# Traffic Light System
#  Ask user to enter traffic light color
traffic_light = input("Enter color: ")

if traffic_light == "Red":
    print("Stop.")
elif traffic_light == "Yellow":
    print("Slow down.")
elif traffic_light == "Green":
    print("Go.")
else :
    print("Invalid color.")     

# Password Strength
# Ask user to enter password
password = (input("Enter the password: "))

if len(password) < 6:
    print("Password too short.")
elif password.isdigit():
    print("Add numbers.")
else:
    print("Strong password.")        





    

        
        





    

