from art import logo
import random

print(logo)
print("Welcome to the 'Guess the Number' challenge!\n")
ready = str(input("Are you ready to start the game? type 'y' or 'n'. ")).lower()

def check_guess(guess, number, chances):
    if guess > number:
        chances -= 1
        message = f"Try lower, {chances} chances left."
    elif guess < number:
        chances -= 1
        message = f"Try higher, {chances} chances left."
    else:
        message = f"You're correct! the number was {number}"
        return chances, True
    print(f"{message}")
    return chances, False

def play_game(chances):
    number = random.randint(0, 100)
    guess = -1
    game_on = False
    while not game_on and chances > 0:
        guess = int(input("What is your guess? "))
        chances , game_on = check_guess(guess, number, chances)



if ready == "y":
    still_play = False
    while not still_play:
        difficulty = input("Choose the difficulty: type hard or easy. ").lower()
        if difficulty == "easy":
            play_game(10)
        else:
            play_game(5)
        ask_again  = input("another round? type 'y' or 'n' ")
        if ask_again == "n":
            still_play = True
else:
    print("See you next time!")
