from art import logo, vs
from db import data
import random
import os
import time


def cls():
    os.system('cls||clear')


def celeb_select():
    """
    Selects a random celebrity from data and returns celebrity's stats, while removing them from database.
    """
    list_num = random.randint(0, len(data) - 1)
    celeb = data[list_num]
    data.pop(list_num)
    return celeb


a = celeb_select()
b = celeb_select()


def presentation():
    def celeb_description(order, celebrity):
        return order + f': {celebrity["name"]}, a {celebrity["description"]}, from {celebrity["country"]}.'
    print(celeb_description("A", a) + vs + celeb_description("B", b))


def more_followers():
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


def game():
    global a, b

    score = 0

    while True:
        while True:
            response = input("\nWho has more followers? Type 'A' or 'B': ")

            if response.upper() != "A" and response.upper() != "B":
                print("Please provide valid answer!")
            else:
                break

        correct = more_followers()

        if response.lower() == correct:
            print("You're right!")
            time.sleep(1.5)
            cls()

            score += 1
            if correct == "b":
                a = b
            b = celeb_select()

            print(logo)
            print(f"Current score: {score}")
            presentation()
        else:
            cls()
            print(logo + f"Sorry, that's wrong. Final score: {score}")

            break


def main():
    global a, b

    while True:
        print(logo)
        presentation()
        game()
        play_again = input("\nWould you like to play again? (Y/n) ")

        if play_again.lower() == "n":
            break
        else:
            a = celeb_select()
            b = celeb_select()
            cls()


if __name__ == "__main__":
    main()
