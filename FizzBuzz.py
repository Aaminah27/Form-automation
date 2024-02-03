import random 

x = [y for y in range(1,101)]
multiples_3=[]
multiples_5=[]
FizzBuzz=[]

for num in x:
    if (num % 3 == 0 and num %5==0):
        FizzBuzz.append(num)
    elif num % 3 == 0:
        #print ("Fizz")
        multiples_3.append(num)
    elif num % 5==0:
        #print("Buzz")
        multiples_5.append(num)
        
print("The Fizz list")
print(multiples_3)
print("The Buzz list")
print(multiples_5)
print("The FizzBuzz list")
print(FizzBuzz)
