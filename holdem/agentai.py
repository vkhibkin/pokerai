import random
import os
import csv
import math

from hand import hand

################################################################################
class distance():
    def __init__(self, d, record):
        self.d = d
        self.record = record
################################################################################
class agentai():

    def __init__(self, ID, dealer):
        self.ID = ID
        self.dealer = dealer
        self.card1 = None
        self.card2 = None
        self.hand = hand(self)

        self.stack = 500
        self.recordOfPastGames = []
        self.gameData = [None,None,None,None,None,None,None,None,None,None,None,None]
        self.gameRound = 12

        #Indecies for the gameData array
        self.PREFLOP_OPPONENT_BET = 0
        self.PREFLOP_HAND_SCORE = 1

        self.FLOP_OPPONENT_BET = 2
        self.FLOP_HAND_SCORE = 3
        self.FLOP_BOARD_SCORE = 4

        self.TURN_OPPONENT_BET = 5
        self.TURN_HAND_SCORE = 6
        self.TURN_BOARD_SCORE = 7

        self.RIVER_OPPONENT_BET = 8
        self.RIVER_HAND_SCORE = 9
        self.RIVER_BOARD_SCORE = 10

        self.RESULT_WIN = 11

        f = open("agentMemory.csv", "r")
        reader = csv.reader(f)
        for record in reader:
            tempAr = []
            for i in range(0, len(record) - 1):
                tempAr.append(float(record[i]))

            if(record[self.RESULT_WIN] == "False"):
                tempAr.append(False)
            else:
                tempAr.append(True)
            self.recordOfPastGames.append(tempAr)
        f.close()

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
    def act(self, gameRound, curentPlayerIndex):
        listOfAllCards = [self.card1, self.card2]
        listOfBoardCards = []
        for c in self.dealer.board:
            if c != None:
                listOfBoardCards.append(c)
                listOfAllCards.append(c)


        handScore = self.CalculateChen(listOfAllCards)
        boardScore = self.CalculateChen(listOfBoardCards)

        if(curentPlayerIndex == 0):
            opponentPlayerIndex = 1
        else:
            opponentPlayerIndex = 0

        opponentBet = self.dealer.curentPot[opponentPlayerIndex]

        if(gameRound == 0):#collect data for preflop
            self.gameData[self.PREFLOP_OPPONENT_BET] = opponentBet
            self.gameData[self.PREFLOP_HAND_SCORE] = handScore
        elif(gameRound == 1):#collect data for flop
            self.gameData[self.FLOP_OPPONENT_BET] = opponentBet
            self.gameData[self.FLOP_HAND_SCORE] = handScore
            self.gameData[self.FLOP_BOARD_SCORE] = boardScore
        elif(gameRound == 2):#collect data for turn
            self.gameData[self.TURN_OPPONENT_BET] = opponentBet
            self.gameData[self.TURN_HAND_SCORE] = handScore
            self.gameData[self.TURN_BOARD_SCORE] = boardScore
        elif(gameRound == 3):#collect data for river
            self.gameData[self.RIVER_OPPONENT_BET] = opponentBet
            self.gameData[self.RIVER_HAND_SCORE] = handScore
            self.gameData[self.RIVER_BOARD_SCORE] = boardScore

        K = 10

        recordData = self.recordOfPastGames
        distances = []

        highestBet = 8;
        lowestBet = 2;
        averageBet = 4;
        curentBetValueIndex = self.PREFLOP_OPPONENT_BET
        #calcualte distances for all the current records
        if(gameRound == 0):#collect data for preflop
            for record in recordData:
                d = 0
                d += math.fabs(self.gameData[self.PREFLOP_OPPONENT_BET] - opponentBet)
                d += math.fabs(self.gameData[self.PREFLOP_HAND_SCORE] - handScore)

                distances.append(distance(d, record))

        elif(gameRound == 1):#collect data for flop
            for record in recordData:
                d = 0
                d += math.fabs(self.gameData[self.FLOP_OPPONENT_BET] - opponentBet)
                d += math.fabs(self.gameData[self.FLOP_HAND_SCORE] - handScore)
                d += math.fabs(self.gameData[self.FLOP_BOARD_SCORE] - boardScore)
                curentBetValueIndex = self.FLOP_OPPONENT_BET
                distances.append(distance(d, record))

        elif(gameRound == 2):#collect data for turn
            for record in recordData:
                d = 0
                d += math.fabs(self.gameData[self.TURN_OPPONENT_BET] - opponentBet)
                d += math.fabs(self.gameData[self.TURN_HAND_SCORE] - handScore)
                d += math.fabs(self.gameData[self.TURN_BOARD_SCORE] - boardScore)
                curentBetValueIndex = self.TURN_OPPONENT_BET
                distances.append(distance(d, record))

        elif(gameRound == 3):#collect data for river
            for record in recordData:
                d = 0
                d += math.fabs(self.gameData[self.RIVER_OPPONENT_BET] - opponentBet)
                d += math.fabs(self.gameData[self.RIVER_HAND_SCORE] - handScore)
                d += math.fabs(self.gameData[self.RIVER_BOARD_SCORE] - boardScore)
                curentBetValueIndex = self.RIVER_OPPONENT_BET
                distances.append(distance(d, record))
        #test changes...
        #figure out if agent is likely to win or loose based on the closest previous games.
        f = 1
        c = 1
        r = 1
        m = 1
        h = 1
        if(len(distances) > K):
            print("were here")
            W = 0
            distances.sort(key = lambda distance: distance.d)

            highestBet = 0;
            lowestBet = 200000;
            averageBet = 0;
            for i in range(0, K):

                recordBet = distances[i].record[curentBetValueIndex]
                if(recordBet > highestBet):
                    highestBet = recordBet

                if(recordBet < lowestBet):
                    lowestBet = recordBet

                averageBet += recordBet

                if(distances[i].record[self.RESULT_WIN] == True):
                    W += 1

            averageBet = math.floor(averageBet / K)

            winingRatio = W / K
            f = 0.08 / math.pow((3 * winingRatio), 1.2)
            if(winingRatio < 0.2):
                c = 0.08 / math.pow((3 * (0.22 - winingRatio)), 1.2)
                r = 0.08 / math.pow((3 * (0.42 - winingRatio)), 1.2)
                m = 0.08 / math.pow((3 * (0.62 - winingRatio)), 1.2)
                h = 0.08 / math.pow((3 * (0.82 - winingRatio)), 1.2)
            elif(winingRatio >= 0.2 and winingRatio < 0.4):
                c = 0.08 / math.pow((3 * (winingRatio - 0.18)), 1.2)
                r = 0.08 / math.pow((3 * (0.42 - winingRatio)), 1.2)
                m = 0.08 / math.pow((3 * (0.62 - winingRatio)), 1.2)
                h = 0.08 / math.pow((3 * (0.82 - winingRatio)), 1.2)
            elif(winingRatio >= 0.4 and winingRatio < 0.6):
                c = 0.08 / math.pow((3 * (winingRatio - 0.18)), 1.2)
                r = 0.08 / math.pow((3 * (winingRatio - 0.38)), 1.2)
                m = 0.08 / math.pow((3 * (0.62 - winingRatio)), 1.2)
                h = 0.08 / math.pow((3 * (0.82 - winingRatio)), 1.2)
            elif(winingRatio >= 0.6 and winingRatio < 0.8):
                c = 0.08 / math.pow((3 * (winingRatio - 0.18)), 1.2)
                r = 0.08 / math.pow((3 * (winingRatio - 0.38)), 1.2)
                m = 0.08 / math.pow((3 * (winingRatio - 0.58)), 1.2)
                h = 0.08 / math.pow((3 * (0.82 - winingRatio)), 1.2)
            else:
                c = 0.08 / math.pow((3 * (winingRatio - 0.18)), 1.2)
                r = 0.08 / math.pow((3 * (winingRatio - 0.38)), 1.2)
                m = 0.08 / math.pow((3 * (winingRatio - 0.58)), 1.2)
                h = 0.08 / math.pow((3 * (winingRatio - 0.78)), 1.2)


            lowestWeight = 1
            if(f < lowestWeight):
                lowestWeight = f
            if(c < lowestWeight):
                lowestWeight = c
            if(r < lowestWeight):
                lowestWeight = r
            if(m < lowestWeight):
                lowestWeight = m
            if(h < lowestWeight):
                lowestWeight = h

            f = math.ceil(f / lowestWeight)
            c = math.ceil(c / lowestWeight)
            r = math.ceil(r / lowestWeight)
            m = math.ceil(m / lowestWeight)
            h = math.ceil(h / lowestWeight)

        actionAr = []

        for j in range(0, f):
            actionAr.append("f")
        for j in range(0, c):
            actionAr.append("c")
        for j in range(0, r):
            actionAr.append("r")
        for j in range(0, m):
            actionAr.append("m")
        for j in range(0, h):
            actionAr.append("h")


        #need to apply the weight to the random values array and submit the actions.
        random.shuffle(actionAr)
        action = actionAr[0]
        if(action == "r"):
            action = "r " + str(lowestBet)
        if(action == "m"):
            action = "r " + str(averageBet)
        if(action == "h"):
            action = "r " + str(highestBet)
        if(action == "f"):
            #if agent opts to fold clear the game data, we wont be storing it
            self.gameData = [None, None, None, None, None, None, None, None, None, None, None, None]

        print("Agent ai action: ",action)
        m = input("agent ai move:")
        return action

    ##################################################
    def sub(self, amount):
        self.stack = self.stack - amount
        return amount

    ##################################################
    def add(self, amount):
        self.stack = self.stack + amount

    ##################################################
    def recordGame(self, isWin):
        print("recordGame...")
        self.gameData[self.RESULT_WIN] = isWin
        self.recordOfPastGames.append(self.gameData)

        file  = open("agentMemory.csv", "a")

        record = ""
        record += str(self.gameData[self.PREFLOP_OPPONENT_BET]) + ","
        record += str(self.gameData[self.PREFLOP_HAND_SCORE]) + ","
        record += str(self.gameData[self.FLOP_OPPONENT_BET]) + ","
        record += str(self.gameData[self.FLOP_HAND_SCORE]) + ","
        record += str(self.gameData[self.FLOP_BOARD_SCORE]) + ","
        record += str(self.gameData[self.TURN_OPPONENT_BET]) + ","
        record += str(self.gameData[self.TURN_HAND_SCORE]) + ","
        record += str(self.gameData[self.TURN_BOARD_SCORE]) + ","
        record += str(self.gameData[self.RIVER_OPPONENT_BET]) + ","
        record += str(self.gameData[self.RIVER_HAND_SCORE]) + ","
        record += str(self.gameData[self.RIVER_BOARD_SCORE]) + ","
        record += str(self.gameData[self.RESULT_WIN]) + "\n"
        file.write(record)
        file.close()

        self.gameData = [None, None, None, None, None, None, None, None, None, None, None, None]

    ##################################################
    def CalculateChen(self, listOfAllCards):
        listOfAllCards = list(listOfAllCards)
        score = 0

        # step 1: Score your highest card only
        highCard = 0
        for x in listOfAllCards:
            if x.ind_val > highCard:
                highCard = x.ind_val

        if highCard == 14:
            score += 10
        elif highCard == 13:
            score += 8
        elif highCard == 12:
            score += 7
        elif highCard == 11:
            score += 6
        else:
            score += (highCard/2)
        score += score

        # step 2: Multiply pairs by 2 of one card’s value
        tempValues = []
        for x in listOfAllCards:
            tempValues.append(x.ind_val)

        tempValues.sort()
        for i in range(1, len(tempValues)):
           if tempValues[i-1]==tempValues[i]:
            if tempValues[i] == 14:
                score += 20
            elif tempValues[i] == 13:
                score += 16
            elif tempValues[i] == 12:
                score += 14
            elif tempValues[i] == 11:
                score += 12
            elif tempValues[i] > 5:
                score += tempValues[i]
            else:
                score += 5

        #step 3: Add 2 points if cards are suited
        tempSuits = []
        for x in listOfAllCards:
            tempSuits.append(x.suit)

        temp = self.uniqueSuits(tempSuits)
        if len(temp) > 1:
            score += 2

        #step 4 Calculate the gap between cards, and assign scores accordingly
        listOfAllCards.sort(key = lambda card: card.ind_val, reverse=True)
        for i in range(0, (len(listOfAllCards)-1) ):
            gap = listOfAllCards[i].ind_val - listOfAllCards[i + 1].ind_val
            gapScore = (14 - gap) * 0.25
            score += gapScore

        #step 5 Round half point scores up
        score = round(score)
        return score

    ##################################################
    def uniqueSuits(self, tempSuits):
        suits = []

        for s in tempSuits:
            if (s in suits) == False:
                suits.append(s)

        return suits


################################################################################
