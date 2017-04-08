import random
import os

################################################################################
class agent():
    def __init__(self, ID, dealer):
        self.ID = ID
        self.dealer = dealer
        self.card1 = None
        self.card2 = None
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
        listOfCards = [self.card1, self.card1]

        for card in board:
            if(card != None):
                listOfCards.append(card)

        self.hand.updateHand(listOfCards)

    ##################################################
    def act(self):
        print("Agent ", self.ID)
        #action = input("make your move: ")

        ## First Iteration AI ##
        action = random.sample(["c","f","r"],1)
        print(action)
        if (action[0] == "r"):
            value = random.random() * self.stack
            print(int(value))
            action = "r " + str(int(value))
        return action
        ########################

        ## Second Iteration AI ##
        rnd = random.random()
        if (rnd < 0.1):
            action = "f"
        elif (rnd < 0.8):
            action = "c"
        else:
            value = random.random() * self.stack
            print(int(value))
            action = "r " + str(int(value))

        return action
        #########################

        
        # if(action == ""):
        #     print("Achtung!!!, Please input a recognized action!")
        #     return self.act()
        # if(action[0] == "h"):
        #     self.help()
        #     return self.act()
        # elif(action[0] == "p"):
        #     self.print()
        #     return self.act()
        # elif(action[0] == "b"):
        #     self.dealer.printBoard("")
        #     return self.act()
        # elif(action[0] != "c" and action[0] != "f" and action[0] != "r"):
        #     print("Achtung!!!, ", action, " is not a recognized action!")
        #     return self.act()

        # return action

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
        print("player: ", self.ID)
        print("hand ", self.card1.name, " ",self.card1.suit, ", ", self.card2.name, " ", self.card2.suit)
        print("stack: ", self.stack)

    ##################################################
    def sub(self, amount):
        self.stack = self.stack - amount
        return amount

    ##################################################
    def add(self, amount):
        self.stack = self.stack + amount

################################################################################