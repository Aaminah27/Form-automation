word = input("Enter a word: ")

#using built-in function to reverse the word and then joining the words
reversed_word = "".join(reversed(word))

print(reversed_word)

if reversed_word==word:
    print(word + " is a palindrome")