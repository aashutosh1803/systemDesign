# Snake and Ladder Game Design

Snake and Ladder is board game. For people, who are not familiar with the game, can visit https://www.ymimports.com/pages/how-to-play-snakes-and-ladders
for getting more information about games and its rules

This is one of basic low level design implementation for Snake and Ladder game. Although its is done in python, same design can also be implemented
in other languages as well

## Design Idea

There are following entities which deal in a Snake and Ladder game
1.Snakes
2.Ladder
3.Player Info
4.Board

We will be having classes for all above entities.

For, Snakes and Ladder classes, we will read their values from constants file in their class constructor
Player Info Class will hold playerId (and may be player name)
Board Class will have info about all snakes and ladder present on board along with all player pieces present on board


As code was made from more a design prespective, output is being shown with different color on terminal for simplicity.
Time Delays has been added to give it a feel like game suspense.


## Running the Code

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python ./game.py

```
