import random
import time, curses

words = ['banana', 'computer', 'elephant', 'strawberry', 'pineapple', 'waterfall', 'butterfly', 'happiness', 'umbrella', 'chocolate']

play_again = 'y'

while play_again.lower() == 'y':
    chosen_word = random.choice(words)
    # Convert the word to a list of characters
    word_list = list(chosen_word)
    # Shuffle the characters
    random.shuffle(word_list)
    # Now join those shuffled characters together
    jumbled_word = ''.join(word_list)
    
    print("The word you have to guess is:", jumbled_word)
    
    start_time = time.time()  # Start the timer
    time_limit = 60  # 1 minute time limit

    while int(time.time() - start_time ) < time_limit:
        guess = input("Can you guess this jumbled word? ")
        
        if guess.lower() == chosen_word:
            print("You have guessed the word correctly! Congratulations!")
            break  # Break out of the loop if the guess is correct
        else:
            print("That's not the correct word. Please try again.")
    else:
        print("Time's up! You took more than 1 minute to guess.")

    play_again = input("Do you want to play again? (Y/N) ")

print("Thank you for playing!")
