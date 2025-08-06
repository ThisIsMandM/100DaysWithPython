import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

final_word = ""
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

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
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You lose!")
    if "_" not in display:
        game_over = True
        print(f"The word is {display},You win.")
    print(stages[lives])
