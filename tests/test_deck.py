import sys
sys.path.insert(0,'..')

from war_game import Deck

def test_deck_size():
	d = Deck()
	size = len(d.cards)
	assert size == 52, "should be 52 cards"

def test_shuffle():
	deck_shuffled = Deck()
	deck_shuffled.shuffle()
	
	deck_regular = Deck()
	assert deck_shuffled.cards != deck_regular.cards, "Shouldn't be equal"

if __name__ == "__main__":
    test_deck_size()
    test_shuffle()
    print("Everything passed")