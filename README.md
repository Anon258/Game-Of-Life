# Game Of Life

This is a repository containing a cellular automaton implementation inspired by John Conway's Game of Life

## _Dependencies_
- Python 3.6.5
- SDL 2.0.10
- Pygame 2.0.0.dev6

### Installation
1. Download the project folder using ```git clone``` 
2. Run ```main.py``` using ```python3.6``` (```3.7``` not supported)

### Description
This is a zero player game based on the theory of Cellular Automaton. The game provides 6 different evolution methods for the world with different rates of growth and patterns. The player can give an initial design of white (alive) cells and proceed to see the evolution or directly start with a random grid (probability of initial populations varies for ease in visualisation)

### Implementation
The game consists of 3 major scenes - *intro.py*, *modes.py* and *game.py* each containing the game loop for displaying the relevant screen with the necessary utilities.
Then there are 2 scripts that handle the actual evolution of the world in *evolution.py* and *rules.py*.
There are also 4 helper scripts containing the global variables and the rendering of text and images and it is all tied down using *main.py*.
