import random 
#importing random library
name = input("what is your name? ")
print("All the best !", name)
words = ['rainy', 'summer', 'winter', 'monsoon', 'autumn', 'spring']
#user can choose one random word from list of words
word_1 = random.choice(words)

print("Guess the letters")
guesses = ''
no_of_turns = 10
#so the user has 10 turns to play the game
while no_of_turns>0:
    failed = 0
    for char in word_1:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
#if the user failed for one time 1 will be incremented
    print()
    if failed == 0:
        print("Yaayyy! You are the winner!")
        print("The word is: ", word_1)
        break
#if user has entered wrong word

    guess = input("Guess a letter: ")
    guesses += guess
    if guess not in word_1:
        no_of_turns -= 1
        print("Sorry! Your guess is wrong!")
        print("You have", no_of_turns, 'more guesses')
        if no_of_turns == 0:
            print("You lost!")
            print("The word is: ", word_1)