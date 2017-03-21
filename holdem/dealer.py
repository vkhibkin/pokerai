from deck import deck
from player import player
from hand import hand


## Need a dictionary of moves here...

## raise amount
## r amount
## f
## fold
## call
## c

##other operational commands comands
##count stack
##count pot
##see cards

#def process_user_input(user_input):




################################################################################
class dealer():
    def __init__(self):
        self.deck = deck()
        self.pot = []
        self.curentPot = []
        self.playerActions = []
        self.board = []
        self.firstPlayerInd = 0



    # how do we keep track of weather betting is finished or not.
    # make an array of what each player bet for each round


    ##################################################
    def deal(self, players, dealerPlayerIndex):
        self.deck.shuffle()
        self.pot = []
        self.curentPot = []
        self.playerActions = []
        self.board = [None, None, None, None, None]

        numberOfPlayers = len(players)

        smallBlindIndex = (dealerPlayerIndex + 1) % numberOfPlayers
        bigBlindIndex = (dealerPlayerIndex + 2) % numberOfPlayers
        curentPlayerIndex = (bigBlindIndex + 1) % numberOfPlayers

        print("small blind index:    ", smallBlindIndex)
        print("big blind index:      ", bigBlindIndex)
        print("current player index: ", curentPlayerIndex)

        for player in players:
            self.pot.append(0)
            self.curentPot.append(0)
            self.playerActions.append("")

            card1 = self.deck.topCard()
            card2 = self.deck.topCard()

            id = player.ID
            card1.ID = id
            card2.ID = id
            player.handCards(card1, card2)


        self.curentPot[smallBlindIndex] += players[smallBlindIndex].sub(1)
        self.curentPot[bigBlindIndex] += players[bigBlindIndex].sub(2)

        return curentPlayerIndex


    # f: fold the round
    # c: call the curent bet on the board
    # r amount: raise the curent bet on the board

    ##################################################
    def handleAction(self, actionToHandle, players, curentPlayerIndex):

        fl = actionToHandle[0]

        print("curentPlayerIndex " , curentPlayerIndex)

        if(fl == "f"):
            self.playerActions[curentPlayerIndex] = "f"

        elif(fl == "c"):
            self.playerActions[curentPlayerIndex] = "c"


            highest_bet = 0
            player_has_bet_so_far = self.curentPot[curentPlayerIndex]

            for p in self.curentPot:
                if(p > highest_bet):
                    highest_bet = p



            amount_to_call = highest_bet - player_has_bet_so_far

            print("amount_to_call ", amount_to_call)

            players[curentPlayerIndex].sub(amount_to_call)
            self.curentPot[curentPlayerIndex] += amount_to_call

        elif(fl == "r"):
            actionArray = actionToHandle.split()
            ammountToRaise = int(actionArray[1])

            highest_bet = 0
            player_has_bet_so_far = self.curentPot[curentPlayerIndex]

            for p in self.curentPot:
                if(p > highest_bet):
                    highest_bet = p

            amount_to_call = highest_bet - player_has_bet_so_far
            amount = ammountToRaise + amount_to_call
            players[curentPlayerIndex].sub(amount)
            self.curentPot[curentPlayerIndex] += amount

        numberOfPlayers = len(players)
        curentPlayerIndex = (curentPlayerIndex + 1) % numberOfPlayers

        return curentPlayerIndex

    ##################################################
    def isBettingFinsihed(self, players, curentPlayerIndex):
        print("Check if betting is finished...");
        #get the highest bet for current pot
        highest_bet = 0
        for p in self.curentPot:
            if(p > highest_bet):
                highest_bet = p

        #for each player check one of two things.
            #has the player bet acted at all
            #has this player bet the highest amount possible
            #has this player folded

        nummber_of_players_wating_to_bet = 0
        for ind in range(0, len(players)):

            print("curentPot: ", self.curentPot[ind], " highest_bet: ", highest_bet, " playerActions: ", self.playerActions[ind])

            if(self.playerActions[ind] != "f" and (self.curentPot[ind] != highest_bet or self.playerActions[ind] == "") ):
                nummber_of_players_wating_to_bet += 1


        print("Number of players waiting to bet: ", nummber_of_players_wating_to_bet)
        if(nummber_of_players_wating_to_bet > 0):
            return False
        else:
            for ind in range(0, len(players)):
                self.pot[ind] += self.curentPot[ind]
                self.curentPot[ind] = 0

            return True

    ##################################################
    def flop(self):
        self.board[0] = self.deck.topCard()
        self.board[1] = self.deck.topCard()
        self.board[2] = self.deck.topCard()

    ##################################################
    def turn(self):
        self.board[3] = self.deck.topCard()

    ##################################################
    def bettingNeeded(self):
        return True

    ##################################################
    def river(self):
        self.board[4] = self.deck.topCard()

    def checkWinner(self, gameCount, players):
        if(gameCount == 0):
            return

        totalWining = 0;
        for p in self.pot:
            totalWining += p

        #check who has folded


        playerHand = []
        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f"):
                players[ind].calculateHand()
                playerHand.append(players[ind].hand)


        if(len(playerHand) == 1):
            playerHand[0].playerParent.add(totalWining)
            return

        playerHand.sort(key = lambda h: h.hand_rank, reverse=True)



        if(playerHand[0].hand_rank == playerHand[1].hand_rank):
            playerHand.sort(key = lambda h: h.highCard, reverse=True)

            if(playerHand[0].highCard == playerHand[1].highCard):
                playerHand[0].playerParent.add(totalWining / 2)
                playerHand[1].playerParent.add(totalWining / 2)
                return

        playerHand[0].playerParent.add(totalWining)


    ##################################################
    def printBoard(self):
        print(self.pot)
        print(self.curentPot)

        cardsOnBoard = []
        for c in self.board:
            if(c != None):
                cardsOnBoard.append(c.name + " " + c.suit)
            else:
                cardsOnBoard.append(None)

        print(cardsOnBoard)

################################################################################