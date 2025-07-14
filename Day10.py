# Create a Contact Book
contact_book = {
    "Asma" : "077 2407892",
    "Amna" : "077 3465 789",
    "Asra" : "077 2404 789"
}
# Then, ask the user to enter a name and display the phone number.
enter_name = input("Enter the name: ")

print(contact_book[enter_name])
print(contact_book.get(enter_name,"invalide name.")) 
     
#  Add a New Key
student_data =  {
    "Name" : "Sara",
    "age" : 20, 
}
# Add new key grade
student_data["grade"] = "A"

# Add new key birth
student_data["Birthday"] = "2004-6-24"

print(student_data)

# Loop Through Dictionary
# create a dictionary of 5 fruits and their prices.
fruits_with_price = {
    "mango" : 100,
    "banana" : 80,
    "orange" : 50,
    "kiwi" :  100,
    "papya" : 250
}
for fruit in fruits_with_price :
    print(fruit, ":", fruits_with_price[fruit])

# count word frequency 
# Ask user to enter a sentence
sentence = input("Enter the sentence: ")

# Count how many times each word appears using a dictionary.
word_list = sentence.split()
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)    


# check if key Exists
# create a dictionary of 3 countries and capitals.
countries_with_capital = {
    "sri lanka" : "sri jayawardana",
    "japan" : "honkon",
    "india" : "new dilli"   
}
country_name = input("Enter the country name: ")
if country_name == "sri lanka":
    print(countries_with_capital["sri lanka"])
elif country_name == "japan":
    print(countries_with_capital["japan"]) 
elif country_name == "india":
    print(countries_with_capital["india"])
else:
    print("Not Found.")  

# Remove an item
# item in a bag
bag_item = {
    "adidas" : 10,
    "nike" : 5,
    "laize" : 6
}  
remove_item = input("Enter which bag item do you want to remove: ")
if remove_item in bag_item:
    del bag_item[remove_item]
    print("{remove_item} removed.")
else:
    print("Item not found in the bag.")    


# Nested Dictionary
# create 2 dictionary of student
students = {
"one_student " : {
    "name" : "Aiza",
    "age" : 12,
    "marks" : 80

},
"second_student":{
    "name" : "Azraan",
    "age" : 13,
    "marks" : 95
    }
}

# print each student marks using loop
for student in students :
    print(students[student]["name"], students[student]["marks"])
    