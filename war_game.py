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


class Hand:
	"""
		A hand of cards. 

		Players will use this class to manage their cards and perform 
		actions during a game. 

		Attributes:
		 cards: A list of lists representing cards.
	"""
	def __init__(self, cards):
		self.cards = cards

	def play_card(self):
		""" 
			Play a card from the hand. 

			It will remove and return the card from the top of the 
			players' deck.

			Returns:
				A list representing a card. [suites, ranks]

			Raises:
				Index Error if the list is empty.
		"""
		return self.cards.pop()

	def add_cards(self, cards):
		"""
			Add cards to Players Hand. 

			Add cards to the beginning of the list. Or bottom of the deck. 

			Args:
				cards: A list of cards. 
		"""
		self.cards = cards + self.cards

	def show_cards(self):
		""" Printing a players card """
		print(self.cards)

	def is_empty(self):
		""" 
			Check if the hand is empty.

			Return true if there are not any cards on the players hand. 

			Returns:
				True or false depending if the hand is empty or not. 
		"""
		return len(self.cards) == 0

	def empty_the_hand(self):
		"""
			Remove all of the cards from the hand. 

			Remove cards and return cards removed. 

			Returns:
				List of cards that were removed from hand. 
		"""
		temp = self.cards.copy()
		self.cards.clear()
		return temp


class Player:
	"""
		A player for the game. 

		Attributes:
			name: The name of the player
			hand: A hand object. The hand the player will use to play the game. 
	"""

	def __init__(self, name, hand):
		self.name = name
		self.hand = hand

	def war_play(self):
		"""
			A war play

			Gives the 3 cards from the top of the deck. 

			It gets the 3 cards. Then, it removes them from the players hand. 
			
			Returns:
				List of cards
		"""
		cards_facing_down = self.hand.cards[len(self.hand.cards)-3:]
		del self.hand.cards[len(self.hand.cards)-3:]
		return cards_facing_down


