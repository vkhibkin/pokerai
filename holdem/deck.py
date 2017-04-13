import random
import os

from card import card

################################################################################
class deck():
    def __init__(self):

        self.topCardInd = 0;

        self.deck_ar = [];
        self.deck_ar.append(card(2, "2", "spd"))
        self.deck_ar.append(card(3, "3", "spd"))
        self.deck_ar.append(card(4, "4", "spd"))
        self.deck_ar.append(card(5, "5", "spd"))
        self.deck_ar.append(card(6, "6", "spd"))
        self.deck_ar.append(card(7, "7", "spd"))
        self.deck_ar.append(card(8, "8", "spd"))
        self.deck_ar.append(card(9, "9", "spd"))
        self.deck_ar.append(card(10, "10", "spd"))
        self.deck_ar.append(card(11, "J", "spd"))
        self.deck_ar.append(card(12, "Q", "spd"))
        self.deck_ar.append(card(13, "K", "spd"))
        self.deck_ar.append(card(14, "A", "spd"))
        self.deck_ar.append(card(2, "2", "hrt"))
        self.deck_ar.append(card(3, "3", "hrt"))
        self.deck_ar.append(card(4, "4", "hrt"))
        self.deck_ar.append(card(5, "5", "hrt"))
        self.deck_ar.append(card(6, "6", "hrt"))
        self.deck_ar.append(card(7, "7", "hrt"))
        self.deck_ar.append(card(8, "8", "hrt"))
        self.deck_ar.append(card(9, "9", "hrt"))
        self.deck_ar.append(card(10, "10", "hrt"))
        self.deck_ar.append(card(11, "J", "hrt"))
        self.deck_ar.append(card(12, "Q", "hrt"))
        self.deck_ar.append(card(13, "K", "hrt"))
        self.deck_ar.append(card(14, "A", "hrt"))
        self.deck_ar.append(card(2, "2", "dmd"))
        self.deck_ar.append(card(3, "3", "dmd"))
        self.deck_ar.append(card(4, "4", "dmd"))
        self.deck_ar.append(card(5, "5", "dmd"))
        self.deck_ar.append(card(6, "6", "dmd"))
        self.deck_ar.append(card(7, "7", "dmd"))
        self.deck_ar.append(card(8, "8", "dmd"))
        self.deck_ar.append(card(9, "9", "dmd"))
        self.deck_ar.append(card(10, "10", "dmd"))
        self.deck_ar.append(card(11, "J", "dmd"))
        self.deck_ar.append(card(12, "Q", "dmd"))
        self.deck_ar.append(card(13, "K", "dmd"))
        self.deck_ar.append(card(14, "A", "dmd"))
        self.deck_ar.append(card(2, "2", "clb"))
        self.deck_ar.append(card(3, "3", "clb"))
        self.deck_ar.append(card(4, "4", "clb"))
        self.deck_ar.append(card(5, "5", "clb"))
        self.deck_ar.append(card(6, "6", "clb"))
        self.deck_ar.append(card(7, "7", "clb"))
        self.deck_ar.append(card(8, "8", "clb"))
        self.deck_ar.append(card(9, "9", "clb"))
        self.deck_ar.append(card(10, "10", "clb"))
        self.deck_ar.append(card(11, "J", "clb"))
        self.deck_ar.append(card(12, "Q", "clb"))
        self.deck_ar.append(card(13, "K", "clb"))
        self.deck_ar.append(card(14, "A", "clb"))

    ##################################################
    def shuffle(self):
        self.topCardInd = 0
        random.shuffle(self.deck_ar)

    ##################################################
    def topCard(self):
        topC = self.deck_ar[self.topCardInd]
        self.topCardInd = self.topCardInd + 1
        return topC
################################################################################