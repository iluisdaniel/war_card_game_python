import sys
sys.path.insert(0,'..')

from war_game import Game


def test_game_set_up():
	print("########## Testing the game is setup correctly")
	g = Game(["Luis", "Computer"])
	assert len(g.player1.hand.cards) == 26 and len(g.player2.hand.cards) == 26, "players cards should be 26"


def test_player1_higher_Card():
	print("########## Testing Player 1 with higher card")
	g = Game(["Luis", "Computer"])
	g.player1.hand.empty_the_hand()
	g.player2.hand.empty_the_hand()

	player1_cards = [['spades', '6'], ['diamonds', '7'], ['spades', '3'], ['hearts', '10']]
	player2_cards= [['clubs', 'K'], ['clubs', '5'], ['diamonds', '8'], ['hearts', '5']]

	g.player1.hand.add_cards(player1_cards)
	g.player2.hand.add_cards(player2_cards)

	player1_deck_size_before = len(g.player1.hand.cards)
	player2_deck_size_before = len(g.player2.hand.cards)

	player1_card = g.player1.hand.play_card()
	player2_card = g.player2.hand.play_card()

	g.check_cards(player1_card, player2_card)

	g.table_cards.clear()

	assert (len(g.player1.hand.cards) == player1_deck_size_before + 1) and (len(g.player2.hand.cards) == player2_deck_size_before - 1), "Player 1 should have one more card, and player two should have one less"

def test_player2_higher_Card():
	print("########## Testing Player 2 with higher card")
	g = Game(["Luis", "Computer"])
	g.player1.hand.empty_the_hand()
	g.player2.hand.empty_the_hand()

	player1_cards = [['diamonds', '6'], ['clubs', '7'], ['spades', '3'], ['spades', '2']]
	player2_cards= [['hearts', 'K'], ['spades', '5'], ['diamonds', '8'], ['diamonds', 'A']]

	g.player1.hand.add_cards(player1_cards)
	g.player2.hand.add_cards(player2_cards)

	player1_deck_size_before = len(g.player1.hand.cards)
	player2_deck_size_before = len(g.player2.hand.cards)

	player1_card = g.player1.hand.play_card()
	player2_card = g.player2.hand.play_card()

	g.check_cards(player1_card, player2_card)

	g.table_cards.clear()

	assert (len(g.player2.hand.cards) == player2_deck_size_before + 1) and (len(g.player1.hand.cards) == player1_deck_size_before - 1), "Player 2 should have one more card, and player 1 should have one less"

def test_cards_on_table():
	print("########## Testing Cards On Table")
	g = Game(["Luis", "Computer"])
	g.player1.hand.empty_the_hand()
	g.player2.hand.empty_the_hand()

	player1_cards = [['spades', '6'], ['diamonds', '7'], ['spades', '3'], ['hearts', '10']]
	player2_cards= [['clubs', 'K'], ['clubs', '5'], ['diamonds', '8'], ['hearts', '5']]

	g.player1.hand.add_cards(player1_cards)
	g.player2.hand.add_cards(player2_cards)

	player1_card = g.player1.hand.play_card()
	player2_card = g.player2.hand.play_card()

	g.check_cards(player1_card, player2_card)

	cards_on_table = g.table_cards.copy()

	g.table_cards.clear()

	assert (player1_card in cards_on_table) and (player2_card in cards_on_table), "cards should be on table"

def test_war():
	print("########## Testing War")
	g = Game(["Luis", "Computer"])
	g.player1.hand.empty_the_hand()
	g.player2.hand.empty_the_hand()

	player1_cards = [['diamonds', '6'], ['clubs', '7'], ['spades', '3'], ['spades', '2'], ['clubs', '10']]
	player2_cards= [['hearts', 'K'], ['spades', '5'], ['diamonds', '8'], ['diamonds', 'A'], ['hearts', '10']]

	g.player1.hand.add_cards(player1_cards)
	g.player2.hand.add_cards(player2_cards)

	player1_deck_size_before = len(g.player1.hand.cards)
	player2_deck_size_before = len(g.player2.hand.cards)

	player1_card = g.player1.hand.play_card()
	player2_card = g.player2.hand.play_card()

	g.check_cards(player1_card, player2_card)

	assert (len(g.player2.hand.cards) == player2_deck_size_before + 5) and (len(g.player1.hand.cards) == player1_deck_size_before - 5), "Player 2 should have 5 more cards, and player 1 should have 5 less"


def test_war_with_no_enough_cards():
	print("########## Testing War No Enough Cards")
	game = Game(["Luis", "Computer"])
	game.player1.hand.empty_the_hand()
	game.player2.hand.empty_the_hand()

	player1_cards = [['diamonds', '6'], ['clubs', '7'], ['clubs', '10']]
	player2_cards= [['hearts', 'K'], ['spades', '5'], ['diamonds', '8'], ['diamonds', 'A'], ['hearts', '10']]

	game.player1.hand.add_cards(player1_cards)
	game.player2.hand.add_cards(player2_cards)

	player1_deck_size_before = len(game.player1.hand.cards)
	player2_deck_size_before = len(game.player2.hand.cards)

	player1_card = game.player1.hand.play_card()
	player2_card = game.player2.hand.play_card()

	print(game.player1.hand.cards)
	print(game.player2.hand.cards)

	game.check_cards(player1_card, player2_card)

	assert (len(game.player2.hand.cards) == player2_deck_size_before + player1_deck_size_before) and (len(game.player1.hand.cards) == 0), "Player 2 should have all the cards, and player 1 should have zero cards"

def test_multiple_wars():
	print("########## Testing Multiple Wars")
	game = Game(["Luis", "Computer"])
	game.player1.hand.empty_the_hand()
	game.player2.hand.empty_the_hand()

	player1_cards = [['clubs', '4'],['diamonds', '4'], ['diamonds', '5'], ['diamonds', '2'], ['diamonds', 'K'], ['clubs', '7'], ['clubs', '3'], ['clubs', '2'], ['clubs', '10']]
	player2_cards=  [['hearts', 'Q'], ['spades', '5'], ['spades', '8'], ['spades', 'A'],['spades', 'K'], ['hearts', '5'], ['hearts', '8'], ['hearts', 'A'], ['hearts', '10']]

	game.player1.hand.add_cards(player1_cards)
	game.player2.hand.add_cards(player2_cards)

	player1_deck_size_before = len(game.player1.hand.cards)
	player2_deck_size_before = len(game.player2.hand.cards)

	player1_card = game.player1.hand.play_card()
	player2_card = game.player2.hand.play_card()

	game.check_cards(player1_card, player2_card)

	cards_on_table = game.table_cards.copy()

	assert (len(cards_on_table) == len(player1_cards) + len(player2_cards)) and (len(game.player2.hand.cards) == player2_deck_size_before + player1_deck_size_before) and (len(game.player1.hand.cards) == 0), "Player 2 should have all the cards, and player 1 should have zero cards"

def test_game():
	print("########## Testing Game")
	game = Game(["Luis", "Computer"])
	game.start()

	assert (len(game.player1.hand.cards) == 52 and len(game.player2.hand.cards) == 0) or (len(game.player2.hand.cards) == 52 and len(game.player1.hand.cards) == 0), "One player should have all of the cards"



if __name__ == "__main__":
	test_game()
	test_game_set_up()
	test_player1_higher_Card()
	test_player2_higher_Card()
	test_cards_on_table()
	test_war()
	test_war_with_no_enough_cards()
	test_multiple_wars()
	print("##########################")
	print("Everything passed")
