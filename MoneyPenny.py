from Boss import Boss


class MoneyPenny(object):
    def enter(self):
        print("You are James Bond.")
        print("You enter MoneyPenny's office.")
        print("You flirt with him for a while, then M interupts.")
        print("She wants to see you immediately.")
        response = input("Do you respond instantly?")
        if response == "yes":
            Boss.enter()
        elif response == "no":
            print("M, angrily wants to know why you are keeping the nation waiting")
            Boss.enter()
        else:
            print("That is not an appropriate response.")
            MoneyPenny.enter(self)


Boss = Boss()
play = MoneyPenny()
play.enter()
