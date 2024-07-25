# Number Guessing Game

## Overview

The **Number Guessing Game** is a simple graphical game implemented using Python's Tkinter library. In this game, players attempt to guess a randomly generated number within a specified range. The game features adjustable difficulty levels and customizable range settings, providing a fun and engaging experience.

## Features

- **Difficulty Levels**: Choose from Easy, Medium, or Hard difficulty levels, which determine the number of attempts allowed.
- **Customizable Range**: Set the minimum and maximum values for the number range.
- **Real-Time Feedback**: Receive immediate feedback on each guess and track the number of attempts.
- **User-Friendly Interface**: Easy-to-use graphical interface built with Tkinter.

## Installation

To run this game, you need to have Python installed on your system. The game uses Tkinter, which is included with the standard Python installation.

## Usage

1. **Set the Difficulty**:
    - Select a difficulty level (Easy, Medium, or Hard). The difficulty determines how many attempts you have to guess the number.

2. **Set the Range**:
    - Enter the minimum and maximum values for the number range.
    - Click "Set range" to generate a random number within this range.

3. **Make a Guess**:
    - Enter your guess in the input field and click "Guess".
    - The game will provide feedback on whether your guess is correct, and how many attempts you have left.

4. **View Results**:
    - If you guess correctly, the game will congratulate you and show the number of attempts it took.
    - If you run out of attempts, the game will reveal the number and end.

## Code Overview

The `GuessingGame` class in `CodXo_1.py` is responsible for initializing the GUI, handling user inputs, and managing the game logic. Key methods include:

- `set_difficulty()`: Configures the number of allowed attempts based on the selected difficulty.
- `set_range()`: Sets the range for the random number and generates a new number to guess.
- `check_guess()`: Evaluates the player's guess, provides feedback, and tracks the number of attempts.
