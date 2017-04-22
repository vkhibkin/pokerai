import os

from deck import deck
from player import player
from hand import hand

################################################################################
class dealer():
    def __init__(self):
        self.deck = deck()
        self.pot = []
        self.curentPot = []
        self.playerActions = []
        self.board = []
        self.firstPlayerInd = 0

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
            players[curentPlayerIndex].sub(amount_to_call)
            self.curentPot[curentPlayerIndex] += amount_to_call

        elif(fl == "r"):
            self.playerActions[curentPlayerIndex] = "r"

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
        highest_bet = 0
        for p in self.curentPot:
            if(p > highest_bet):
                highest_bet = p

        nummber_of_players_not_folded = 0
        nummber_of_players_wating_to_bet = 0
        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f" ):
                nummber_of_players_not_folded += 1
            if(self.curentPot[ind] != highest_bet or self.playerActions[ind] == "" ):
                nummber_of_players_wating_to_bet += 1

        if(nummber_of_players_wating_to_bet > 0 and nummber_of_players_not_folded > 1):
            return False
        else:
            for ind in range(0, len(players)):
                self.pot[ind] += self.curentPot[ind]
                self.curentPot[ind] = 0

            return True

    ##################################################
    def flop(self, players, dealerPlayerIndex):

        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f"):
                self.playerActions[ind] = ""

        self.board[0] = self.deck.topCard()
        self.board[1] = self.deck.topCard()
        self.board[2] = self.deck.topCard()
        numberOfPlayers = len(players)
        curentPlayerIndex = (dealerPlayerIndex + 1) % numberOfPlayers
        return curentPlayerIndex

    ##################################################
    def turn(self, players, dealerPlayerIndex):
        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f"):
                self.playerActions[ind] = ""
        self.board[3] = self.deck.topCard()
        numberOfPlayers = len(players)
        curentPlayerIndex = (dealerPlayerIndex + 1) % numberOfPlayers
        return curentPlayerIndex

    ##################################################
    def river(self, players, dealerPlayerIndex):
        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f"):
                self.playerActions[ind] = ""
        self.board[4] = self.deck.topCard()
        numberOfPlayers = len(players)
        curentPlayerIndex = (dealerPlayerIndex + 1) % numberOfPlayers
        return curentPlayerIndex

    ##################################################
    def bettingNeeded(self, players):
        nummber_of_players_not_folded = 0

        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f" ):
                nummber_of_players_not_folded += 1

        if(nummber_of_players_not_folded > 1):
            return True
        else:
            return False

    ##################################################
    def checkWinner(self, gameCount, players):
        if(gameCount == 0):
            return

        totalWining = 0;
        for p in self.pot:
            totalWining += p

        totalWiningString = "$"+str(totalWining)
        playerHand = []
        for ind in range(0, len(players)):
            if(self.playerActions[ind] != "f"):
                players[ind].calculateHand()
                playerHand.append(players[ind].hand)

        if(len(playerHand) == 1):
            playerHand[0].playerParent.add(totalWining)
            print("Player", playerHand[0].playerParent.ID," wins:",totalWiningString)
            a = input("ok: ")
            return

        playerHand.sort(key = lambda h: h.hand_rank, reverse=True)
        if(playerHand[0].hand_rank == playerHand[1].hand_rank):
            playerHand.sort(key = lambda h: h.highCard, reverse=True)
            if(playerHand[0].highCard == playerHand[1].highCard):
                playerHand[0].playerParent.add(totalWining / 2)
                playerHand[1].playerParent.add(totalWining / 2)
                print("Players tie.")
                a = input("ok: ")
                return

        print("Player", playerHand[0].playerParent.ID," wins:",totalWiningString)
        playerHand[0].playerParent.add(totalWining)
        a = input("ok: ")

    ##################################################
    def printBoard(self, roundName):
        pot = [0,0]
        pot[0] = self.pot[0] + self.curentPot[0]
        pot[1] = self.pot[1] + self.curentPot[1]

        total = pot[0] + pot[1]
        total = "$"+str(total)
        pot[0] = "$"+str(pot[0])
        pot[1] = "$"+str(pot[1])

        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------")
        print(roundName)
        print("Current pot value: ", total)
        print("Player 1 bet:", pot[0])
        print("Player 2 bet:", pot[1])

        cardsOnBoard = ""

        for c in self.board:
            if(c != None):
                cardsOnBoard += " " + c.name + " " + c.suit
            else:
                cardsOnBoard += " *"

        print("Board: ", cardsOnBoard)
        print("")

################################################################################