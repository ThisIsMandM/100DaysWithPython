import random

from hangman_words import word_list
from hangman_art import stages, logo
lives = 6
print(logo)
chosen_word = random.choice(word_list)


placeholder = ""

for place in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_guesses = []
false_guesses = []
while not game_over:

    print(f"****************************<{lives}> LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_guesses or guess in false_guesses:
        print(f"You already guessed letter {guess}, try something lese")


    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_guesses.append(guess)
            elif letter in correct_guesses:
                display += letter
            else:
                display += "_"
                false_guesses.append(guess)

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            if lives == 0:
                game_over = True

                print(f"***********************YOU LOSE**********************\nThe word was {chosen_word}" )

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")


        print(stages[lives])
