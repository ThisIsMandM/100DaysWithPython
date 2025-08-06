import random
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
place= ""
for placeholder in range(len(chosen_word)):
    place += "_"

game_over = False
correct_guesses= []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            correct_guesses.append(guess)
            display += letter
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1

    if "_" not in display:
        game_over = True
        print("You win.")

final_word = str(correct_guesses)
print(final_word)
