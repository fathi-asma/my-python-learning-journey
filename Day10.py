# Create a Contact Book
contact_book = {
    "Asma" : "077 2407892",
    "Amna" : "077 3465 789",
    "Asra" : "077 2404 789"
}
# Then, ask the user to enter a name and display the phone number.
user_enter_name = input("Enter the name: ")

if(user_enter_name == "Asma"):
    print(contact_book["Asma"])
elif(user_enter_name == "Amna"):
    print(contact_book["Amna"])
elif(user_enter_name == "Asra"):
    print(contact_book["Asra"])
else:
    print("Invalide name.")        