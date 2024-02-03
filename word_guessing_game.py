import random

countries =['Pakistan', 'Malaysia', 'Kuwait', 'Palestine']

user_name = input('Enter your name: ')
print('Hi ' + user_name + ', you have to guess the country in 10 tries')

# Picking up a country randomly
country = random.choice(countries)
country = country.lower()
answer = ''

for i in range(10):  # Range starts from 0, so it's already 10 tries
    print("Try number:", i + 1, '\n')
    guessed_correctly = True
    for c in country:
        if c in answer:
            print(c, end='')
        else:
            print('_', end='')
            guessed_correctly = False
    print()  # Print a newline after showing the country
    
    if guessed_correctly:
        print("You Won")
        break
    
    guess = input("Enter a letter: ").lower()
    answer += guess

if not(guessed_correctly):
    print("Wrong guess, country was:", country)
