from AloneInYourCell import AloneInYourCell

from sys import exit



class Casino(object):

    def enter(self):

        print("Blofed is here with his much younger, glamourous girlfriend.")
        print("He is playing Poker.")
        print("He asks you to join him.")
        print("Do you have a stronger hand?")
        cards = input("Enter a number between 1 and 10:")
        intcards = int(cards)
        if intcards > 5:
            print("You have beaten Blofeld at Poker.")
            print("He is not very happy.")
            print("However, his girlfriend is now madly in love with you.")
            print("This makes him doubly unhappy.")
            print("He angrily shouts at his henchmen to lock you up.")
            AloneInYourCell.enter()


        elif cards <=int(5):
            print("Blofed has beaten you at Poker.")
            print("He is very happy.")
            print("You have lost a lot of taxpayers money.")
            print("Blofed laughs and shouts at his henchmen to lock you up.")
            AloneInYourCell.enter()

        else:
            print("That is not an appropriate response.")
            cards = input("Enter a number between 1 and 10:")

Casino = Casino()
