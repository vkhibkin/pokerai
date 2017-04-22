import random
import os
import numpy as np
import math
from hand import hand


################################################################################
class agent():
    def __init__(self, ID, dealer, level):
        self.ID = ID
        self.dealer = dealer
        self.card1 = None
        self.card2 = None
        self.hand = hand(self)
        self.stack = 500
        self.level = level
    
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
        if self.level==1:
            action = random.sample(["c","f","r"],1)
            print(action)
            if (action[0] == "r"):
                value = random.random() * self.stack
                #print(int(value))
                action = "r " + str(int(value))
            
        ########################

        ## Second Iteration AI ##
        elif self.level==2: 
            rnd = random.random()
            if (rnd < 0.1):
                action = "f"
            elif (rnd < 0.8):
                action = "c"
            else:
                value = random.random() * self.stack
                print(int(value))
                action = "r " + str(int(value))

            

        ## Third Iteration AI ##
        elif self.level==3:
            chenScore=0
            chenScore=agent.CalculateChen(self)         
            if chenScore>12:
                action = "r " + str(round(.95 * self.stack))
            elif chenScore>11:
                action = "r " + str(round(.8 * self.stack))
            elif chenScore>10:
                action = "r " + str(round(.6 * self.stack))
            elif chenScore> 9:
                action = "r " + str(round(.4 * self.stack))
            else:
                action = "f"
            #print(action)    

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


    def CalculateChen(self):
        board = self.dealer.board
        listOfCards = [self.card1, self.card2]
        listOfAllCards =[]
        score = 0
        for x in board:
            if x != None:
                listOfAllCards.append(x)
        # step 1: Score your highest card only
        highCard=0
        for x in listOfCards:
            if x.ind_val>highCard:
                highCard=x.ind_val
        if highCard==14:
            score+=10
        elif highCard == 13:
            score+=8
        elif highCard == 12:
            score+=7
        elif highCard == 11:
            score+=6
        else:
            score+=(highCard/2)
        

        # step 2: Multiply pairs by 2 of one card’s value
        tempValues=[]
        for x in listOfCards:
            tempValues.append(x.ind_val)
        tempValues.sort()
        for i in range(1,len(tempValues)):
           if tempValues[i-1]==tempValues[i]:
            if tempValues[i]==14:
                score+=20
            elif tempValues[i] == 13:
                score+=16
            elif tempValues[i] == 12:
                score+=14
            elif tempValues[i] == 11:
                score+=12
            elif tempValues[i] > 5:
                score+=tempValues[i]
            else:
                score+=5  
         #step 3: Add 2 points if cards are suited
        tempSuits=[]
        for x in listOfCards:
            tempSuits.append(x.suit)
        temp=np.unique(tempSuits)
        if len(temp)>1:
            score+=2

        #step 4 Subtract points if their is a gap between the two cards.
        gap=abs(listOfCards[0].ind_val-listOfCards[1].ind_val)
        if gap<5:
            score-=gap
        else:
            score-=5
        #step 5 Add 1 point if there is a 0 or 1 card gap and both cards are lower than a Q
            if gap>1 and listOfCards[0].ind_val<12 and listOfCards[1].ind_val<12:
                score+=1
        #step 6 Round half point scores up

        score=round(score)
        return score
    
        
                
                  
        
    










    
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
        print("agent: ", self.ID)
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
