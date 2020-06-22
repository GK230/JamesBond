from sys import exit
from random import randint


class BombRoom(object):

    def enter():
        print("There is a bomb here, ticking away.")
        print("A voice is repeatedly saying 'Destruction Imminent'.")
        print("You have to stop the countdown before it explodes.")
        print("Otherwise it will destroy the world")
        number = input("Guess the 3-digit code that will disable the bomb.")
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The bomb has been disabled - you have saved the world.")
            print("Blofed's girlfriend is so impressed she leaves him for you.")
            print("The End.")
            print("Will James Bond return again?")
            replay = input("In other words, do you want to play again?")
            if replay == "yes":
                import MoneyPenny
                MoneyPenny.enter()
            elif replay == "no":
                exit(1)
            else:
                    print("That is not an appropriate response.")
                    print("Do you want to play again?")

        elif guess != code:
            print("The bomb explodes destroying the planet.")
            print("You failed in your mission.")
            print("M's final thought is that you were obviously the wrong person for the job.")
            print("Do you want to prove M wrong?")
            replay = input("In other words, do you want to play again?")
            if replay == "yes":
                import MoneyPenny
                MoneyPenny.enter()
            elif replay == "no":
                    exit(1)
            else:
                    print("That is not an appropriate response.")
                    print("Do you want to play again?")
