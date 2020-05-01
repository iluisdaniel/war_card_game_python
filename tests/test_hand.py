import sys
sys.path.insert(0,'..')

from war_game import Hand
from war_game import Deck

def test_card_play_size():
	d = Deck()
	h = Hand(d.cards)
	card = h.play_card()
	assert len(h.cards) == 51, "should be 51 cards"

def test_card_play():
	d = Deck()
	h = Hand(d.cards)
	card = h.play_card()
	assert not card in h.cards, "should not be in hand"

def test_empty_hands():
	d = Deck()
	h = Hand(d.cards)
	cards = h.empty_the_hand()
	assert h.is_empty() and len(cards) == 52, "should be empty and temp cards should be 52"

def test_adding_cards():
	d = Deck()
	h = Hand(d.cards)
	temp_cards = []
	temp_cards.append(h.play_card())
	temp_cards.append(h.play_card())
	temp_cards.append(h.play_card())
	h.add_cards(temp_cards)
	assert len(h.cards) == 52, "should be 52 cards"


if __name__ == "__main__":
	test_card_play_size()
	test_card_play()
	test_empty_hands()
	test_adding_cards()
	print("Everything passed")