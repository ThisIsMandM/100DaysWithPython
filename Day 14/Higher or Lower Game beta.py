from art import logo, vs
import random
from game_data import data

print(logo)

game_on = False
def which_is():
    global game_on
    random_name1 = random.choice(data)
    random_name2 = random.choice(data)
    print(f"Compare A: {random_name1['name']}, a {random_name1['description']}, from {random_name1['country']}")
    print(vs)
    print(f"Compare B: {random_name2['name']}, a {random_name2['description']}, from {random_name2['country']}")

    user_guess = str(input("Who has more followers? Type A or B \n")).upper()
    result = follower_check(random_name1, random_name2)
    if user_guess == result :
        print("Correct!")
    else:
        print("Wrong, it was the other one!")
    another_game = input("Do you want to have another guess? type y or n \n").lower()
    if another_game != "y":
        game_on = True
def follower_check(random_name1, random_name2):
    if random_name1['follower_count'] > random_name2['follower_count']:
        return "A"
    elif random_name1['follower_count'] < random_name2['follower_count']:
        return "B"




while not game_on:
    which_is()