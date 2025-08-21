from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_images[dice_num])


# Problem: the list starts from 0 so when there are 6 things in it, it goes from 0 to 5.