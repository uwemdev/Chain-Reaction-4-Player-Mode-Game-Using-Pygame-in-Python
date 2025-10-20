# Chain Reaction 4 Player Game

An interactive and strategic desktop game built with **Python** and the **Pygame** library. Challenge your friends in this exciting 4-player adaptation of the classic Chain Reaction game.


## About the Game

Chain Reaction is a turn-based strategy game played on a grid. The goal is to be the last player standing by eliminating your opponents' orbs.

**How to Play:**
- Players take turns placing their colored orbs on the grid.
- You can place an orb on an empty cell or a cell you already occupy.
- When a cell reaches its critical mass (number of orbs equals its number of adjacent cells), it explodes!
- Upon exploding, the orbs propagate to all adjacent cells, converting them to your color and potentially causing a chain reaction of explosions.
- Eliminate all other players to win!

This project is an excellent exercise for understanding game logic, grid-based mechanics, and the Pygame library.

## Features

- **4-Player Local Multiplayer**: Play with up to 4 friends on a single machine.
- **Strategic Gameplay**: Simple rules with deep tactical possibilities.
- **Dynamic Chain Reactions**: Watch as a single move triggers a massive cascade across the board.
- **Colorful and Clear UI**: Intuitive interface with distinct colors for each player.
- **Turn-Based Mechanics**: Perfect for taking your time and planning your next move.

## Installation & How to Run

Follow these steps to get the game running on your machine:

### Prerequisites
- **Python 3.x** must be installed on your computer.
  - If you don't have it, download it from [python.org](https://www.python.org/downloads/).

### Steps
1. **Download the Source Code**
   - Clone this repository or download the ZIP file and extract it.

2. **Install Pygame**
   - The game requires the Pygame library. Open your command prompt/terminal and run:
     ```bash
     pip install pygame
     ```

3. **Run the Game**
   - Navigate to the project directory in your terminal.
   - Run the main Python file:
     ```bash
     python chain_reaction.py
     ```
   - Alternatively, you can open `chain_reaction.py` in Python IDLE or your favorite IDE (like VS Code, PyCharm) and run it from there.

## How to Play

1. The game will start with a grid and a display showing whose turn it is (Player 1, 2, 3, or 4).
2. On your turn, click on a valid cell to place your orb.
3. Plan your moves carefully to trigger chain reactions that will overwhelm your opponents!
4. The last player with orbs remaining on the board wins the game.

## Project Information

- **Language:** Python
- **Library:** Pygame
- **Type:** Desktop Application
- **Database:** None

## Disclaimer

This project was developed for educational purposes. The source code is free to use and modify. Enjoy learning and coding!

