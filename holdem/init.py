import sys
import os

from dealer import dealer
from player import player
from agent import agent
from card import card
from hand import hand

################################################################################
def init():


    h = hand(1)
    J = 11
    Q = 12
    K = 13
    A = 14

    testHand = []





    # testHand.append(card(5, "5", "dmd"))
    # testHand.append(card(5, "5", "hrt"))
    # testHand.append(card(4, "4", "clb"))
    # testHand.append(card(2, "2", "dmd"))
    # testHand.append(card(3, "3", "spd"))
    # testHand.append(card(Q, "Q", "c;b"))
    # testHand.append(card(A, "A", "hrt"))

    # testHand.append(card(3, "5", "dmd"))
    # testHand.append(card(3, "5", "hrt"))
    # testHand.append(card(10, "4", "clb"))
    # testHand.append(card(9, "2", "dmd"))
    # testHand.append(card(10, "3", "spd"))
    # testHand.append(card(Q, "Q", "c;b"))
    # testHand.append(card(3, "A", "hrt"))

    # h.updateHand(testHand)
    # print(h.hand_rank, ", ", h.highCard)

    start_table()



################################################################################

def start_table():
    players = []
    dealerObj = dealer()

    level= int(input("Player 1 level (1-3) or person (0): "))

    
    if level==1:
        players.append(agent(1, dealerObj,1))
    elif int(level)==2:
        players.append(agent(1, dealerObj,2))
    elif level==3:
        players.append(agent(1, dealerObj,3))
    else:
        players.append(player(1, dealerObj))
    print(players[0])
    level= int(input("Player 2 level (1-3) or person (0): "))
    if level==1:
        players.append(agent(2, dealerObj,1))
    elif level==2:
        players.append(agent(2, dealerObj,2))
    elif level==3:
        players.append(agent(2, dealerObj,3))
    else:
        players.append(player(2, dealerObj))
    #players.append(player(3, dealerObj))


    #flag to keep track of which round of the game is curently in progress
    #A.K.A. prflop, flop, river, turn etc.
    gameRound = 0
    #strictly for curiosity keep track of how many games have been played
    gameCount = 0

    #this is the player that holds the dealer chip
    #next person is the small blind
    dealerPlayerIndex = -1

    while(True):
        ## if start of new game
        if(gameRound == 0):
            #first check who won the previous round which will destribute the winnings to that player
            dealerObj.checkWinner(gameCount, players)
            dealerPlayerIndex = (dealerPlayerIndex + 1) % len(players)
            gameCount += 1
            # deal the cards which will reset the pot the game and all other stuff.
            curentPlayerIndex = dealerObj.deal(players, dealerPlayerIndex)
            dealerObj.printBoard("Pre-flop round: ")
        if(gameRound == 1):
            curentPlayerIndex = dealerObj.flop(players, dealerPlayerIndex)
            dealerObj.printBoard("Flop round: ")
        if(gameRound == 2):
            curentPlayerIndex = dealerObj.turn(players, dealerPlayerIndex)
            dealerObj.printBoard("Turn round: ")
        if(gameRound == 3):
            curentPlayerIndex = dealerObj.river(players, dealerPlayerIndex)
            dealerObj.printBoard("River round: ")

        #Make sure each player updates their hand value
        for p in players:
            p.calculateHand()

        # start the betting loop
        betting_finished = False


        #check if betting is needed at all maybe only one player left unfolded
        if(dealerObj.bettingNeeded(players) == True):
            while(betting_finished == False):
                # promt player for action
                action = players[curentPlayerIndex].act(gameRound)
                curentPlayerIndex = dealerObj.handleAction(action, players, curentPlayerIndex)
                betting_finished = dealerObj.isBettingFinsihed(players, curentPlayerIndex)

            gameRound = (gameRound + 1) % 4

        else:
            #if all but one players folded skip to first round and rest the game
            gameRound = 0




    print("starting new table...")

################################################################################
init()
