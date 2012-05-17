# Bowling

Records bowling scores

## Features
* Flexible number of players
* Ensures unique player names
* Scoreboard displays per frame scores and running total
* Tracks team total
* Tracks bonuses for strikes and spares
* Determines winner of game

## How to play

`python bowling.py`

First you will be prompted to enter the player names.  Player names must be unique.  Enter each player name and press enter.  When you have no more player names remaining press enter again without entering any text.

For each frame you will be asked to enter the number of pins that were knocked down for each bowl.  The scoreboard will be displayed at the end of each frame.

The name of the winner is displayed at the end of the game.

## TODO

* Improve validation on 2nd roll of frame to ensure can only bowl as many remamining pins.
	* or simulate real life where machine may incorrectly rerack, and allow a spare.
	* show the remaining pin count on the prompt
* Improve scoreboard layout
	* Show in boxout
	* Show separate player total rather than just last entry in running total
	* Show X for strike and / for spare
* Use ansi colouring for error/result messages

## Requirements
No dependencies.  Python 2.5+  
`python bowling.py`  
`python bowling_test.py`



