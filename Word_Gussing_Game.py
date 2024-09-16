import random  # We need random to pick a word from the list

# This is our list of secret words
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']

# We choose one secret word from the list
word = random.choice(word_bank)

# This is what the player will see at the start: all blanks
guessedWord = ['_'] * len(word)

# The player has 10 chances to guess the letters
attempts = 10

# This is the game loop that keeps going until the player is out of chances
while attempts > 0:
    # Show the player the current state of the word
    print('\nCurrent word: ' + ' '.join(guessedWord))

    # Ask the player to guess a letter
    guess = input('Guess a letter: ').lower()

    # If the guessed letter is in the secret word
    if guess in word:
        # We replace the blanks with the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')  # Tell the player they guessed right!
    else:
        # If the guess is wrong, we take away one chance
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))  # Show how many tries are left

    # If all letters are guessed, the player wins
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break  # End the game if the player guesses all letters
else:
    # If the player runs out of chances, they lose
    print('\nYou\'ve run out of attempts! The word was: ' + word)

# The second loop below is unnecessary, so we don't need to keep it

while attempts > 0:
   
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
    else:
      print('\nYou\'ve run out of attempts! The word was: ' + word)