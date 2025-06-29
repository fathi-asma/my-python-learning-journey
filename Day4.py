# create a List and print
fruits = ["Apple", "Mango", "Banana", "papaya", "Lemon"]
print(fruits)

# Access Elements
print(fruits[0])
print(fruits[4])

# Add an Item
fruits.append("kiwi")
print(fruits)

# Remove an Item
fruits.remove("Apple")
print(fruits)

# Check for Item
check = input("Enter a fruit name: ")
if check in fruits :
    print("Enter fruit in the list.")
else :
    print("Enter fruit is not in list.")    

# List Length
print(len(fruits))

# Sort the List
fruits.sort()
print(fruits)

# Reverse the List
fruits.reverse()
print(fruits)

# Insert at a Specific Position
fruits.insert(2,"Apple")
print(fruits)

# Pop an Item
fruits.pop(4)
print(fruits)

# Clear the List
fruits.clear()
print(fruits)

# Copy the List
fruits1 = fruits.copy()
print(fruits1)

# Extend the List
fruits.extend("Mango")
print(fruits)

# Index of an Item
print(fruits.index("Mango"))
print(fruits.index("Apple"))
print(fruits.index("Banana"))

# Count Occurrences
fruits.count("Mango")
print(fruits)
