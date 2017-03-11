
################################################################################
class hand():
   def __init__(self):
       self.fullHand = []
       self.bestHand = []


       # 9 Royal flush
       # 8 Straight flush
       # 7 Four of a Kind
       # 6 Full house
       # 5. Flush
       # 4 Straight
       # 3 Three of a kind
       # 2 Two pair
       # 1 Pair
       # 0 Nothing
       self.hand_rank = 0

       #range from 2 to 14
       self.highCard = 2

       self.playerID = None

################################################################################