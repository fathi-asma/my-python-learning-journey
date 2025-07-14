# count words in a sentence
# ask use to enter sentence
enter_sentence = input("Enter the sentence: ")
word_count = 0
for word in enter_sentence.split():
    word_count += 1
    print(word_count)

# find the largest number in a list
numbers = [10, 20, 30, 40, 50, 60] 
for number in numbers:
      largest_number = (max(numbers))
print("largest number is: ", largest_number)  
 

# check prime numbers between 1 and 50
def is_prime(num):
     if num <= 1:
          return False
     for i in range(2,num):
          if num % i == 0:
               return False
     return True 
for n in range(1, 51):
     if is_prime(n):
        print(n) 
   
# Find the numbers divisible by 3 and 5
for num in range(1, 101):
     if num % 3 == 0 and num % 5 == 0:
          print(num)