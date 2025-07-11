# print numbers 1 to 10 using while loop
i = 1
while i <= 10:
    print(i)
    i = i+1

# print all even numbers from 2 to 20
i = 2
while i <= 20:  
    print(i)
    i = i+2
   

# ask user to enter number until type 0 then stop the loop
while True:
    i = int(input("Enter the numbers and if you want to break enter 0: "))
    if(i == 0):
        print("Done")
        break
    else:
        print("Enter number is: ", i)


# keep asking user to enter a password until they enter correct one
while True:
    enter_password = input("Enter the correct password: ")
    if(enter_password == "python1234"):
        print("Successfull.")
        break
    else:
        print("Faild, try to enter correct password.") 


# sum all numbers from 1 to 100 using while loop
i = 1
total = 0

while i <= 100:
    total += i
    i = i+1
print("Summation: ", total)    
