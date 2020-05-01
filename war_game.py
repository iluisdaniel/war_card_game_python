import random

suits = ['spades','hearts','diamonds', 'clubs']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']


class Deck:
	"""
		A Deck of cards.

		It will create a deck of 52 cards. 

		A card is represented like this [suites, ranks].

		To shuffle the deck use shuffle()

		Attributes:
		 cards: A list of lists representing cards.
	"""
	
	def __init__(self):
		self.cards = []
		self.build_deck()

	def build_deck(self):
		""" 
			Itereates through the lists of suits and ranks to create a list of cards. 
		"""
		for suit in suits:
			for rank in ranks:
				self.cards.append([suit, rank])

	def shuffle(self):
		""" Shuffes the deck of cards """
		random.shuffle(self.cards)
