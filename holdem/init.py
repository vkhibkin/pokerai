import sys
from dealer import dealer
from player import player
from card import card

################################################################################

def init():

    dealerObj = dealer()

    J = 11
    Q = 12
    K = 13
    A = 14

#    testHand = []
#    testHand.append(card(5, "5", "dmd"))
#    testHand.append(card(5, "5", "hrt"))
#    testHand.append(card(5, "4", "clb"))
#    testHand.append(card(2, "2", "dmd"))
#    testHand.append(card(8, "9", "spd"))
#    testHand.append(card(Q, "Q", "c;b"))
#    testHand.append(card(A, "A", "hrt"))



#    print(dealerObj.checkTwoPair(testHand))
#    print(dealerObj.checkThreeOfKind(testHand))
#    print(dealerObj.checkFourOfKind(testHand))


#    testHand = []
#    testHand.append(card(5, "5", "dmd"))
#    testHand.append(card(5, "5", "dmd"))
#    testHand.append(card(8, "9", "spd"))
#    testHand.append(card(Q, "Q", "dmd"))
#    testHand.append(card(A, "A", "hrt"))
#    testHand.append(card(5, "4", "dmd"))
#    testHand.append(card(2, "2", "dmd"))

#    print(dealerObj.checkFlush(testHand))



    testHand = []
    testHand.append(card(2, "5", "dmd"))
    testHand.append(card(3, "5", "dmd"))
    testHand.append(card(4, "9", "spd"))
    testHand.append(card(Q, "Q", "dmd"))
    testHand.append(card(6, "A", "hrt"))
    testHand.append(card(5, "4", "dmd"))
    testHand.append(card(3, "2", "dmd"))

    print(dealerObj.checkStraight(testHand))









    #if(sys.argv[1] == "start"):
    #    start_table()
    #elif(sys.argv[1] == "join"):
    #    join_table()
    #else:
    #    print("no starting argument provided")


################################################################################

def start_table():
    players = []
    dealerObj = dealer()
    players.append(player(1, dealerObj))
    players.append(player(2, dealerObj))
    players.append(player(3, dealerObj))


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
        if(gameRound == 1):
            dealerObj.flop()
            dealerObj.printBoard()
        if(gameRound == 2):
            dealerObj.turn()
            dealerObj.printBoard()
        if(gameRound == 3):
            dealerObj.river()
            dealerObj.printBoard()







        # start the betting loop
        betting_finished = False

        #check if betting is needed atall maybe only one player left unfolded
        if(dealerObj.bettingNeeded() == True):
            while(betting_finished == False):
                print("moo")
                # promt player for action
                action = players[curentPlayerIndex].act()
                curentPlayerIndex = dealerObj.handleAction(action, players, curentPlayerIndex)
                betting_finished = dealerObj.isBettingFinsihed(players, curentPlayerIndex)


            gameRound = (gameRound + 1) % 4

        else:
            #if all but one players folded skip to first round and rest the game
            gameRound = 0


            # process player action by giving it the dealer
            # dealer returns if betting is finished which
            # automaticaly update the betting_finished flag
            # increment player to act



        # determine which round of the game were in. there are
            # 0 preflop
            # 2 flop
            # 3 turn
            # 4 river



    print("starting new table...")
################################################################################
def join_table():
    print("joining existing table...")


################################################################################

init()

##   https://wiki.python.org/moin/TcpCommunication
##   we also ave a join game method
    ##while(True):
    ##    person = input('Enter your name: ')
    ##    print('Hello', person)