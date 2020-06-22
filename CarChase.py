from Casino import Casino
from sys import exit


class CarChase(object):

    def enter(self):

        print("There is a sports car here.")
        print("You get inside, and start driving around a Swiss mountain.")
        print("The henchmen are chasing you in an ordinary car.")
        speed = input("Do you drive fast and recklessly or slow and stealthily?")
        if speed == "fast and recklessly":
            print("You drive off the cliff and the car explodes.")
            print("The henchmen laugh at you incomptent driving.")
            replay = input("Do you want to play again?")
            if replay == "yes":
                import MoneyPenny
                MoneyPenny.enter()
            elif replay == "no":
                 exit(1)
            else:
                 print("That is not an appropriate response.")
                 print("Do you want to play again?")

        elif speed == "slow and stealthily":
            print("The henchmen starts firing bullets at your car.")
            print("You evade the henchmen with your amazing driving skills.")
            print("You eventually pull up outside a casino in your tuxedo.")
            Casino.enter()


        else:
            print("That is not an appropriate response.")
            CarChase.enter(self)
