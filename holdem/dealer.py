from deck import deck
from player import player



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
            player.hand(card1, card2)


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

        #check who has folded

        playerHandRank = []
        for ind in range(0, len(players)):
            playerHandRank.append(0)

            if(self.playerActions[ind] == "f"):
                playerHandRank[ind] = -1
            else:
                totalHand = [
                self.board[0],
                self.board[1],
                self.board[2],
                self.board[3],
                self.board[4],
                players[ind].card1,
                players[ind].card2]








        # 1. Royal flush
        # 2. Straight flush
        # 3. Four of a Kind
        # 4. Full house
        # 5. Flush
        # 6. Straight
        # 7. Three of a kind
        # 8. Two pair
        # 9. Pair

        #NOTE: dont forget to check for ties


    ##################################################
    #def checkRoyalFlush(self, totalHand):

    #This one is easy there are only 4 combintation that match.
    #check for those combinations.


    ##################################################
    #def checkStraightFlush(self, totalHand):

    #check streight, put the streight in to a separate array
    # then check that array for a flush.

    ##################################################
    def checkFourOfKind(self, totalHand):
        totalHand.sort(key = lambda card: card.ind_val)

        trips_found = 0;
        for i in range(0, len(totalHand) - 3):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val
               and totalHand[i].ind_val == totalHand[i + 2].ind_val
                and totalHand[i].ind_val == totalHand[i + 3].ind_val):
                return True

        return False

    ##################################################
    def checkFullHouse(self, totalHand):
        totalHand.sort(key = lambda card: card.ind_val, reverse=True)
        for card in totalHand:
            print(card.ind_val)
        print("moo...")





        #TODO:
        #what if its a situation where we have 3 of a kind and 3 of kind together.
        #not sure if that needs to be handled. might not make a difference

        #2,2,3,3,3 vs 2,2,4,4,4,
        #2,2,3,3,3 vs 2,2,2,4,4,



        three_of_a_kind_found = False
        #first find three of a kind and remove from deck.
        for i in range(0, len(totalHand) - 2):
            #print(totalHand[i].ind_val)
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val and totalHand[i].ind_val == totalHand[i + 2].ind_val):
                three_of_a_kind_found =  True

                print(totalHand[i].ind_val,",",totalHand[i + 1].ind_val,",",totalHand[i + 2].ind_val)

                totalHand.pop(i)
                totalHand.pop(i)
                totalHand.pop(i)

                break


        print("moo2...")
        for card in totalHand:
            print(card.ind_val)

        #then try to find a pair and remove from hand
        if(three_of_a_kind_found):
            for i in range(0, len(totalHand) - 1):
                if(totalHand[i].ind_val == totalHand[i + 1].ind_val):
                    return True




        return False

    #fisr check for a pair and remove it from array put it in a diferent array
    #then find a 3 of a kind and remove that.


    ##################################################
    def checkFlush(self, totalHand):
        totalHand.sort(key = lambda card: card.suit)
        for i in range(0, len(totalHand) - 4):
            if(totalHand[i].suit == totalHand[i + 1].suit and totalHand[i].suit == totalHand[i + 2].suit
                and totalHand[i].suit == totalHand[i + 3].suit and totalHand[i].suit == totalHand[i + 4].suit):
                return True

        return False

    ##################################################
    def checkStraight(self, totalHand):
        totalHand_new_list = list(totalHand)
        indexes_to_pop = []

        for i in range(0, len(totalHand)):
            for j in range(i+1, len(totalHand)):

                if(totalHand[i].ind_val == totalHand[j].ind_val):
                    #print(i,"-",j,": ",totalHand[i].ind_val,"==",totalHand[j].ind_val)
                    indexes_to_pop.append(j)
                #else:
                    #print(i,"-",j,": ",totalHand[i].ind_val,"!=",totalHand[j].ind_val)

        for ind in indexes_to_pop:
            totalHand_new_list.pop(ind)

        totalHand_new_list.sort(key = lambda card: card.ind_val)

        if(len(totalHand_new_list) < 5):
            return False


        elif(len(totalHand_new_list) == 5):
            for i in range(0, len(totalHand_new_list) - 6):

                if(totalHand_new_list[i].ind_val == (totalHand_new_list[i + 1].ind_val - 1)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 2].ind_val - 2)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 3].ind_val - 3)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 4].ind_val - 4)):
                    return True
        elif(len(totalHand_new_list) == 6):

            for i in range(0, len(totalHand_new_list) - 5):


                if(totalHand_new_list[i].ind_val == (totalHand_new_list[i + 1].ind_val - 1)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 2].ind_val - 2)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 3].ind_val - 3)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 4].ind_val - 4)):
                    return True
        elif(len(totalHand_new_list) == 7):
            for i in range(0, len(totalHand_new_list) - 4):

                if(totalHand_new_list[i].ind_val == (totalHand_new_list[i + 1].ind_val - 1)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 2].ind_val - 2)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 3].ind_val - 3)
                    and totalHand_new_list[i].ind_val == (totalHand_new_list[i + 4].ind_val - 4)):
                    return True

        return False

    ##################################################
    def checkThreeOfKind(self, totalHand):
        totalHand.sort(key = lambda card: card.ind_val)

        for i in range(0, len(totalHand) - 2):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val and totalHand[i].ind_val == totalHand[i + 2].ind_val):
                return True

        return False

    ##################################################
    def checkTwoPair(self, totalHand):
        #NOTE this algorythm will treat a 3 of a kind as 2 pair
        #and fiirther 4 of a kind as a 3 pair
        #however that is ok for now since will be first checking a hand
        #for theose

        #TODO if there are 3 sets of pairs then we need to make sure to grab the highest 2.

        #TODO: Comapring two hands with two paris if both sets of pairs are the same
        # for example 2,2,3,3,A and 2,2,3,3,K the high card is the Ace so it should win,
        #this is a fringe situation but must be handled.

        totalHand.sort(key = lambda card: card.ind_val)

        pairs_found = 0;
        for i in range(0, len(totalHand) - 1):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val):
                pairs_found += 1


        return pairs_found

    ##################################################
    def checkPair(self, totalHand):
        #TODO this compares each card to it self, so always returns true
        for C in totalHand:
            for c in totalHand:
                if(c.ind_val == C.ind_val):
                    return True

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