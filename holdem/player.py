import copy
import re

from hand import hand

################################################################################
class player():
    def __init__(self, ID, dealer):
        self.ID = ID
        self.dealer = dealer
        self.card1 = None
        self.card2 = None
        self.hand = hand(self)

        self.stack = 500

    ##################################################
    def handCards(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        #h get print out of all the actions
        #p get print out of curent state

    ##################################################
    def calculateHand(self):
        board = self.dealer.board
        listOfCards = [self.card1, self.card2]

        for card in board:
            if(card != None):
                listOfCards.append(card)

        self.hand.updateHand(listOfCards)

    ##################################################
    def act(self, gameRound):
        #print("Player ", self.ID, "make your move." )
        self.print()
        action = self.processAction()
		
        return action

    def processAction(self):
        action = input(": ")
        if(action == ""):
            print("Achtung!!!, Please input a recognized action!")
            return self.processAction()
        if(action[0] == "h"):
            self.help()
            return self.processAction()
        elif(action[0] == "p"):
            self.print()
            return self.act()
        elif(action[0] == "b"):
            self.dealer.printBoard("")
            return self.processAction()
        elif(action[0] == "r"):
            pattern = re.compile("^r\s[0-9]+$")
            if(pattern.match(action)):
                action = action
            else:
                print("Achtung!!!, Please input a recognized action!")
                return self.processAction()

        elif(action[0] != "c" and action[0] != "f"):
            print("Achtung!!!, ", action, " is not a recognized action!")
            return self.processAction()

        return action


    # Dictionary of possible player actions
    #
    # h: prints out this dictionary as a string
    # p: prints out the current player state
    # b: print out the curent board state
    #
    # f: fold the round
    # c: call the curent bet on the board
    # r amount: raise the curent bet on the board

    def help(self):
        print("# Dictionary of possible player actions")
        print("#")
        print("# h: prints out this dictionary as a string")
        print("# p: prints out the current player state")
        print("# b: print out the curent board state")
        print("#")
        print("# f: fold the round")
        print("# c: call the curent bet on the board")
        print("# r amount: raise the curent bet on the board")

    ##################################################
    def print(self):
        print("")
        stack = "$"+str(self.stack)

        print("Player: ", self.ID)
        print("Current hand:", self.card1.name,"",self.card1.suit, ",", self.card2.name, "", self.card2.suit)
        print("Stack:",stack)

    ##################################################
    def sub(self, amount):
        self.stack = self.stack - amount
        return amount

    ##################################################
    def add(self, amount):
        self.stack = self.stack + amount

    ##################################################
    def recordGame(self, isWin):
        a = 1

################################################################################