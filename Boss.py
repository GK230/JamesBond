from BondGirl import BondGirl
from sys import exit


class Boss(object):



    def enter(self):

        print("M asks you to sit down.")
        print("She says there is a very dangerous mission.")
        print("However, it is suitable for a man of your talents.")
        play = input("Do you accept?")
        if play == "yes":
            BondGirl.enter()
        elif play == "no":
            print("You coward, you don't like foreign travel")
            exit(1)
        else:
            print("That is not an appropriate response.")
            Boss.enter(self)



BondGirl= BondGirl()
