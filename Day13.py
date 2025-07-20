# ask user to enter base number 
def base_num():
     return int(input("Enter the base number: "))

# ask user to enter power number  
def pow_num():
     return int(input("Enter the power number: "))

# calculate the results using for loop    
def raise_to_power():
    base = base_num()
    power = pow_num()
    result = 1
    for index in range(power):
        result = result * base
    return result         
print("The final result is: ", raise_to_power())

# update the raise_to_power()function to handle the following cases
# if the power is 0 return 1 and if the power is negative return recirocal of the result
def raise_to_power():
     base = base_num()
     power = pow_num()
     result = 1
     for index in range(abs(power)):
        if power < 0:
             return 1 / result
        else:
             result = result * base
             return result
print("The final result is: ", raise_to_power())        
