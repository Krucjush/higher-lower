import art
import random
import game_data
import os

def clean():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def compare(a, b):
    if a > b:
        return "a"
    elif a < b:
        return "b"
    else:
        return "c"
    
score = 0
game_over = False
a = random.choice(game_data.data)
while not game_over:
    clean()
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(f"Followers: {a['follower_count']}")
    print(art.vs)
    b = random.choice(game_data.data)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess not in ["a", "b"]:
        exit(f"{guess} is not a valid guess\nAborting...")
    higher = compare(a["follower_count"], b["follower_count"])
    if guess == higher or higher == "c":
        a = b
        score += 1
    else:
        game_over = True
clean()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")