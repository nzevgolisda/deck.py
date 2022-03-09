
import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffled = []
        self.deck = []
        self.figures = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.seasons = ['X', 'Y', 'Z', 'W']
        self.playerNames = ['A1', 'B1', 'C1', 'D1']
        self.playerHands = [[], [], [], []]
    def createCards(self):
        for season in self.seasons:
            for figure in self.figures:
                card = Card(figure, season)
                self.cards.append(card)
        self.deck = self.cards
        return self
    def shuffleCards(self):
        used = []
        unused = self.deck
        while len(used) < len(unused):
            j = random.randint(0, 51)
            if j not in used:
                pass
            elif j in used:
                while j in used:
                    j = random.randint(0, 51)
            used.append(j)
        for i in used:
            self.shuffled.append(self.deck[i])
        self.deck = self.shuffled
        return self
    def drawCard(self):
        self.card = self.deck.pop(0)
        return self
    def dealFirstHand(self):
        i = 0
        for i in range(len(self.playerNames)):
            for j in range(2):
                self.drawCard()
                hand = self.playerHands[i]
                hand.append(self.card)
        self.board = []
        return self
    def fillBoard(self, k):
        for j in range(k):
            self.drawCard()
            self.board.append(self.card)
        return self

    def __str__(self):
        s = 'Deck: '
        if len(self.deck)>0:
            for card in self.deck:
                s += str(card)
        else:
            s = '{emptyDeck}'
        s+='\n'
        #############
        q = ''
        j = 0
        if len(self.playerHands[0])>0:
            while j < 4:
                q += 'Hand of player '+str(self.playerNames[j])+': '
                hand = self.playerHands[j]
                for card in hand:
                    q+=str(card)
                j += 1
                q+='\n'
        else:
            q = '{emptyHands}'
        ######################
        r = ''
        j = 0
        if len(self.board)>0:
            r += 'Board: '
            for card in self.board:
                r+=str(card)
        else:
            r += '{emptyBoard}'
        r+='\n'
        return s+q+r
