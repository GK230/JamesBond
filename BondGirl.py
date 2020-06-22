from CarChase import CarChase
# from MoneyPenny import MoneyPenny



class BondGirl(object):

    def enter(self):
        print("You fly into an exotic location.")
        print("You enter your hotel room.")
        print("There is a woman here.")
        print("She has a foreign accent.")
        print("You need information from the woman about Blofed.")
        device = input("Do you torture her or try to seduce her?")
        if device == "torture":
            print("The woman dies, vowing not to say a word.")
            print("You are arrested for murder.")
            print("The Foreign Office says 'if you have committed a crime in a foreign country you will be liable to the laws of that country'")
            print("You claim you are MI6.")
            print("M denies ever knowing you.")
            print("You spend the rest of your life 'Banged up abroad'")
            print("You even appear on the TV show.")
            replay = input("Do you want to play again?")
            print(replay)
            if replay == "yes":
                import MoneyPenny
                MoneyPenny.enter(self)

                #replay.enter(self)
            elif replay == "no":
                    exit(1)

        elif device == "seduce":
            print("The woman tries to kill you, put you manage to escape.")
            CarChase.enter(self)
        else:
            print("That is not an appropriate response.")
            BondGirl.enter(self)
# MoneyPenny = MoneyPenny()
