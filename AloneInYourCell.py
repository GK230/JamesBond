from BombRoom import BombRoom
from sys import exit


class AloneInYourCell(object):

    def enter(self):

        print("You are alone in your cell.")
        print("There is nothing here.")
        equipment = input("Which one of Q's devices do you use to escape: your latest Omega watch, your fully armed fountain pen, or your exploding briefcase?")
        if equipment == "Omega watch":
            print("The watch self destructs, blowing you up into little pieces.")
            replay = input("Would you like to play again?")
            if replay == "yes":
                MoneyPenny.enter()
            elif replay == "no":
                exit(1)
            else:
                print("That is not an appropriate response.")
                print("Would you like to play again?")

        elif equipment == "fully armed fountain pen":
            print("You furiously shake your fountain pen, but is has run out of liquid explosive.")
            print("You remain locked up until you die of starvation - your mission is never mentioned.")
            replay = input("Would you like to play again?")
            if replay == "yes":
                MoneyPenny.enter()
            elif replay == "no":
                    exit(1)
            else:
                print("That is not an appropriate response.")
                print("Would you like to play again?")

        elif equipment == "exploding briefcase":
            print("You throw your exploding briefcase at heavy steel door.")
            print("It bursts open.")
            print("You run outside.")
            BombRoom.enter()

        else:
            print("That is not an appropriate response.")
            print("What equipment do you choose?")

AloneInYourCell = AloneInYourCell()
