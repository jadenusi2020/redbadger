# REDBADGER

# Mars Robot Simulator

A Python program that simulates robot movements on the surface of Mars based on instructions.

## Features

- **Grid Management**: Rectangular grid with configurable boundaries (0,0 to max_x,max_y)
- **Robot Control**: Support for turning (L/R) and moving (F) commands
- **Safety System**: Scent markers prevent multiple robots from falling off at same positions
- **Input Validation**: Enforces coordinate limits (max 50) and instruction length (max 100 chars)
- **Error Handling**: Handling of invalid input formats

## Movement Commands

- **L**: Turn left 90° (changes orientation only)
- **R**: Turn right 90° (changes orientation only)  
- **F**: Move forward one grid point in current direction

## Orientations

- **N**: North (increasing y-direction)
- **S**: South (decreasing y-direction)
- **E**: East (increasing x-direction)
- **W**: West (decreasing x-direction)

## Constraints

- Maximum coordinate value: 50
- Maximum instruction length: 100 characters
- Grid boundaries: 0 to specified upper-right coordinates

## Installation & Usage

### Method 1: Direct Input
python main.py
Then enter input manually

### Method 2: Input via text file
python main.py<input.txt
Enter input in a text file similar to input.txt file
