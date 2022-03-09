from card import Card
from deck import Deck

deck = Deck()
deck.createCards()
deck.shuffleCards()
deck.dealFirstHand()
deck.fillBoard(2)
print(deck)
