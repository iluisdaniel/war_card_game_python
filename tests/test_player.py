import sys
sys.path.insert(0,'..')

from war_game import Hand
from war_game import Deck
from war_game import Player

def test_cards_size_from_war_play():
	d = Deck()
	player = Player("Luis", Hand(d.cards))
	cards_facing_down = player.war_play()
	assert len(cards_facing_down) == 3, "should be 3 cards"

def test_players_hand_size_after_war():
	d = Deck()
	player = Player("Luis", Hand(d.cards))
	cards_facing_down = player.war_play()
	assert len(player.hand.cards) == 49, "should be 49 cards"

if __name__ == "__main__":
    test_players_hand_size_after_war()
    test_cards_size_from_war_play()
    print("Everything passed")