# War Battle

A card game for two players using Python.

## Rules of the game

The objective of the game is to win all of the cards.

The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with 
the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.

If the two cards played are of equal value, then there is a "war". Both players place the next  three cards of their 
pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards 
on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set 
of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

[More Info](https://en.wikipedia.org/wiki/War_(card_game))

## Dependencies

* **Python3**

## Running the game

 To start a game you need to initialize a Game object with the name of the two players that are going to participate. And then run the start() function. 
 
``` python 
game = Game(["Luis", "Computer"])
game.start()
```

To run the game:

```
python3 war_game.py
```

## Testing

From the tests directory run the test you want to run.

```
tests: python3 test_game.py
```

## Notes

- When there is a war battle, we remove three cards from the player's hand instead of one. This way the game will be completed faster.
- The cards won by a player are added at the bottom of their hand without shuffling them.
- From time to time, we will encounter a deck without War battles in them. This will make a game to last a lot of time, sometimes even infinite. I believe that this will be resolved by shuffling the cards won by a player. However, this doesn't happen very often. 

## TODO

- **Shuffle cards won by players**. Create a deck with the cards won by a player. When their hand is empty: take the deck of cards won, shuffle them, and then add them to the player's hand. And repeat.
- **Better logging**. Right now, we are just printing messages to the console. With a better logging feature we could have a cleaner interface for playing and testing. 
- **Better User Interface**. It will be fun to create a GUI interface or even a website that players could interact with. Maybe using Kivy or Django.

