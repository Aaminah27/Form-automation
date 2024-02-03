import random, math

high = int(input("Enter the upper limit\t"))
low = int (input("Enter the lower limit\t"))

number = random.randint(low,high)

no_of_guesses = round(math.log(high - low +1 ,2))

print("You have "+ str(no_of_guesses) + " guesses to guess the number")

count = 0

while (count < no_of_guesses):
    count +=1

    user_guess = int(input("Your guess? "))

    if (user_guess == number):
        print ("You have guessed it correctly, Great job")
        print("Number is %d",number)
        break
    elif(user_guess < number):
        print("Your guess is less than the actual number, try again")
    
    elif(user_guess > number):
        print("Your guess is greater than the actual number, try again")

if count >= no_of_guesses:
    print("\nThe number is %d" % number)
    print("\tBetter Luck Next time!")