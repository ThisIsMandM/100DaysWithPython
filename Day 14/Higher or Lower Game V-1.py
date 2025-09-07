from art import logo, vs
import random
from game_data import data

print(logo)


game_on = False

def pick_two():
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    return a, b
def which_is():
    global game_on
    a, b = pick_two()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")

    user_guess = str(input("Who has more followers? Type A or B \n")).upper()
    while user_guess != "A" or "B":
        user_guess = str(input("Wrong input! only Type A or B \n")).upper()
        
    result = follower_check(a, b)
    if user_guess == result :
        print("Correct!")
    else:
        print("Wrong, it was the other one!")
    another_game = input("Do you want to have another guess? type y or n \n").lower()
    if another_game != "y":
        game_on = True
def follower_check(a, b):
    if a['follower_count'] > b['follower_count']:
        return "A"
    elif a['follower_count'] < b['follower_count']:
        return "B"




while not game_on:
    which_is()