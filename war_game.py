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


class Game:
	"""
	 The War Game.

	 Creates a game with all the funcionality to set it up and to play it.

	 To initialize it, it needs the name of two players. Then it will create two Players
	 with half of a shuffled deck of cards. 

	 Attributes:
  	   table_cards: A list of cards that are currently being played, or are in the table.
	   player1: A player that will play the game.
	   player2: Second player for the game. 
	"""

	def __init__(self, players):
		deck = Deck()
		deck.shuffle()
		self.table_cards = []
		self.player1 = Player(players[0], Hand(deck.cards[26:]))
		self.player2 = Player(players[1], Hand(deck.cards[:26]))

	def start(self):
		"""
		  Starts a game.

		  It will play a card everytime until a player ends up with an empty hand.

		  After the players play their cards, it will compare them to see who wins. 

		  After a player with empty hands is found it will check the results. 
		"""
		print("Starting game")
		count = 0
		while not self.player1.hand.is_empty() and not self.player2.hand.is_empty():
			print("Turn " + str(count))


			print("Player1 number of cards " + str(len(self.player1.hand.cards)))
			print("Player2 number of cards " + str(len(self.player2.hand.cards)))
			count = count + 1

			player1_card = self.player1.hand.play_card()
			player2_card = self.player2.hand.play_card()

			print("Player1 playing " + str(player1_card))
			print("Player2 playing " + str(player2_card))

			self.check_cards(player1_card, player2_card)

			self.empty_table()
			print("Cards in table " + str(self.table_cards))
			print("#########################################")


		self.check_results()
			

	def check_cards(self, player1_card, player2_card):
		"""
		  Check the cards players played 

		  It compares two cards and it will add the cards on the table to 
		  whoevers card's is higher. 

		  In case the cards are the same it will do WAR!! It will take 3 cards from
		  each player, add them to the table, and then the process will repeat again 
		  with a new cards. 

		  If a players doesn't have enough cards to play WAR. It will empty their hands,
		  and put the on the table. And then the other player will gain the cards from the table.

		  Args:
		    player1_card: A card played from Player1
		    player2_card: A card played from Player2
		  Raises:
		    IndexError: If the cards provided are not in the right format [suit. rank]
		"""
		self.table_cards.append(player1_card)
		self.table_cards.append(player2_card)

		print("Cards in table " + str(self.table_cards))

		if ranks.index(player1_card[1]) > ranks.index(player2_card[1]):
			print("Player 1 WON!")
			self.player1.hand.add_cards(self.table_cards)
		elif ranks.index(player1_card[1]) < ranks.index(player2_card[1]):
			print("Player 2 WON!")
			self.player2.hand.add_cards(self.table_cards)
		else:
			print("WAR!!!")
			if self.player1.hand.is_empty() or self.player2.hand.is_empty():
				return

			if len(self.player1.hand.cards) < 4:
				print("Player 1 doesn't have enough cards!")
				player1_last_cards = self.player1.hand.empty_the_hand()
				self.table_cards = self.table_cards + player1_last_cards
				self.player2.hand.add_cards(self.table_cards)
				return
			elif len(self.player2.hand.cards) < 4:
				print("Player 2 doesn't have enough cards!")
				player2_last_cards = self.player2.hand.empty_the_hand()
				self.table_cards = self.table_cards + player2_last_cards
				self.player1.hand.add_cards(self.table_cards)
				return

			player1_facing_down_cards = self.player1.war_play()
			player2_facing_down_cards = self.player2.war_play()

			self.table_cards = self.table_cards + player1_facing_down_cards + player2_facing_down_cards

			player1_second_card = self.player1.hand.play_card()
			player2_second_card = self.player2.hand.play_card()

			print("Player1 playing " + str(player1_second_card))
			print("Player2 playing " + str(player2_second_card))

			self.check_cards(player1_second_card, player2_second_card)

	def check_results(self):
		""" 
		  Display which player is the winner by checking their hands. 
		"""
		if self.player1.hand.is_empty():
			print("Congrats! Player 2 WON!!!")
		elif self.player2.hand.is_empty():
			print("Congrats! Player 1 WON!!!")
		else:
			print("Error!!!!")

	def empty_table(self):
		"""
		  Empty the cards on the table. 
		"""
		self.table_cards = []

	def display_game_info(self):
		"""
		  Prints the information of the game into the console. 
		"""
		print("##### WELCOME TO WAR ##############")
		print("Player 1: %s" % self.player1.name)
		print("Player 2: %s" % self.player2.name)
		print("--------------------------------------")

		rules = """\nRules:\n
The objective of the game is to win all of the cards.

The deck is divided evenly among the players, giving each a down stack. In unison, 
each player reveals the top card of their deck—this is a "battle"—and the player with 
the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.

If the two cards played are of equal value, then there is a "war". Both players place the next  three cards of their 
pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards 
on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set 
of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.
"""

		print(rules)

if __name__ == "__main__":
	g = Game(["Luis", "Computer"])
	g.display_game_info()
	input("Press Enter to continue...")
	g.start()