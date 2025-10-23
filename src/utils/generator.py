# /*=====Start Change Task 3 & 4=====*/
import os
import csv
import random
from fifteenpuzzle import FifteenPuzzleState

def createRandomFifteenPuzzle(moves=25):
    """
    moves: number of random moves to apply.

    Creates a random 15-puzzle by applying
    a series of 'moves' random moves to a solved puzzle.
    """
    puzzle = FifteenPuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])  # Solved state
    for i in range(moves):
        # Execute a random legal move
        puzzle = puzzle.result(random.choice(puzzle.legalMoves()))
    return puzzle

def generate_and_save_scenarios(scenarios_file, num_puzzles=5000, moves=25):
    """
    Generates random 15-puzzles and saves them to a CSV file.

    """
    puzzles = [createRandomFifteenPuzzle(moves).cells for _ in range(num_puzzles)]

    # Save to CSV
    with open(scenarios_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PuzzleID', 'State'])  # Header
        for idx, puzzle in enumerate(puzzles):
            writer.writerow([idx + 1, str(puzzle)])  # Save puzzle as string
    print(f"Generated and saved {num_puzzles} puzzles to {scenarios_file}")

# /*=====End Change Task 3 & 4 =====*/
