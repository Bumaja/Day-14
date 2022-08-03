import random
import os

from game_data import data
from art import logo, vs

def data_choose(set_of_data):
    # Randomowy wybór elementu. Zwrócenie stringa z reprezentacją elementów.
    to_compare = random.choice(set_of_data)
    return to_compare
    # return f"{to_compare['name']}, {to_compare['description']}, from {to_compare['country']}"

clear = lambda: os.system("clear")
a = data_choose(data)
b = data_choose(data)
score = 0

def game(dict_a, dict_b, user_score):

    # Game layout
    print(logo)
    compare_a = f"{dict_a['name']}, {dict_a['description']}, from {dict_a['country']}"
    followers_a = dict_a['follower_count']
    print(f"Compare A: {compare_a}.")
    
    print(vs)
    compare_b = f"{dict_b['name']}, {dict_b['description']}, from {dict_b['country']}"
    print(f"Compare B: {compare_b}.")
    followers_b = dict_b['follower_count']
    
    who_has_more = input("Who has much followers?: Type 'A' or 'B'")

    # Game logic
    if who_has_more == 'A' and followers_a <= followers_b or who_has_more == 'B' and followers_b <= followers_a:
        print(f"You lose! Your score: {user_score}.")        
    if who_has_more == 'A' and followers_a > followers_b:
        # Assigning new data to 'dict_b', increasing 'user_score', clearing screan and calling the game function
        dict_b = data_choose(data)
        user_score += 1
        clear()
        game(dict_a, dict_b, user_score)
    elif who_has_more == 'B' and followers_b > followers_a:
        # Assigning 'dict_b' to variable 'dict_a', assigning new data to 'dict_b', increasing 'user_score' by 1, clearing the screen and calling the game function
        dict_a = dict_b
        dict_b = data_choose(data)
        user_score += 1
        clear()
        game(dict_a, dict_b, user_score)

game(a, b, score)
