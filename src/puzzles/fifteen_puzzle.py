# fifteenpuzzle.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import search
import random


# Module Classes

class FifteenPuzzleState:
    """
    The Fifteen Puzzle (4x4 grid) is an extension of the 8-puzzle.

    This class defines the mechanics of the 15-puzzle itself.
    The task of recasting this puzzle as a search problem is left to
    the FifteenPuzzleSearchProblem class.
    """

    def __init__(self, numbers):
        """
        Constructs a new fifteen puzzle from an ordering of numbers.

        numbers: a list of integers from 0 to 15 representing an
        instance of the fifteen puzzle. 0 represents the blank space.

        Example configuration (solved state):
        -------------
        | 1 | 2 | 3 | 4 |
        -------------
        | 5 | 6 | 7 | 8 |
        -------------
        | 9 | 10| 11| 12|
        -------------
        | 13| 14| 15|   |  <-- 0 represents the blank space
        -------------
        """
        # Initialize the grid and blank space location
        self.cells = []
        numbers = numbers[:]  # Make a copy to avoid side-effects.
        numbers.reverse()

        # =====Start Change Task 1.1=====
        # Adjust for 4x4 grid (Fifteen Puzzle)
        for row in range(4):  # Change from 3 to 4 rows
            self.cells.append([])
            for col in range(4):  # Change from 3 to 4 columns
                self.cells[row].append(numbers.pop())
                if self.cells[row][col] == 0:
                    self.blankLocation = row, col  # Track blank space
        # =====End Change Task 1.1=====

    def isGoal(self):
        """
        Checks if the puzzle is in its goal state (solved state) for a 4x4 grid:

        -------------
        | 1 | 2 | 3 | 4 |
        -------------
        | 5 | 6 | 7 | 8 |
        -------------
        | 9 | 10| 11| 12|
        -------------
        | 13| 14| 15| 0 |  <-- 0 represents the blank space
        -------------

        Returns True if the current state is the goal state.
        """
        current = 1  # Start with 1 since 0 is the blank space.

        # /*=====Start Change Task 1.2 =====*/
        # Adjust for 4x4 grid
        for row in range(4):  # Iterate over 4 rows
            for col in range(4):  # Iterate over 4 columns
                if row == 3 and col == 3:  # Bottom-right corner should be 0 (blank space)
                    if self.cells[row][col] != 0:
                        return False
                else:
                    if self.cells[row][col] != current:
                        return False
                    current += 1
        # /*=====End Change Task 1.2 =====*/
        return True

    def legalMoves(self):
        """
        Returns a list of legal moves from the current state.

        Moves consist of moving the blank space 'up', 'down', 'left', or 'right'.
        """
        moves = []
        row, col = self.blankLocation

        # /*=====Start Change Task 1.3 =====*/
        # Adjust boundaries for 4x4 grid
        if row != 0:  # Move up
            moves.append('up')
        if row != 3:  # Move down
            moves.append('down')
        if col != 0:  # Move left
            moves.append('left')
        if col != 3:  # Move right
            moves.append('right')
        # /*=====End Change Task 1.3 =====*/

        return moves

    def result(self, move):
        """
        Returns a new FifteenPuzzleState with the current state and blankLocation
        updated based on the provided move.

        The move should be a string drawn from 'legalMoves'.
        Illegal moves will raise an exception.
        """
        row, col = self.blankLocation

        # Determine the new position of the blank space after the move
        if move == 'up':
            newrow = row - 1
            newcol = col
        elif move == 'down':
            newrow = row + 1
            newcol = col
        elif move == 'left':
            newrow = row
            newcol = col - 1
        elif move == 'right':
            newrow = row
            newcol = col + 1
        else:
            raise ValueError("Illegal Move")

        # Create a copy of the current puzzle
        # /*=====Start Change Task 1.4 =====*/
        # Adjust to initialize 16 tiles for the 4x4 grid
        newPuzzle = FifteenPuzzleState([0] * 16)
        newPuzzle.cells = [row[:] for row in self.cells]  # Deep copy of current state
        # /*=====End Change Task 1.4 =====*/

        # Swap the blank space with the target tile
        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]
        newPuzzle.blankLocation = newrow, newcol

        return newPuzzle

    # Utilities for comparison and display
    def __eq__(self, other):
        """
        Checks if two FifteenPuzzleStates are equal (i.e., have the same configuration).
        """
        # /*=====End Change Task 1.5 =====*/
        # Adjust for comparison of 4 rows (Fifteen Puzzle)
        for row in range(4):
            if self.cells[row] != other.cells[row]:
                return False
        # /*=====End Change Task 1.5 =====*/
        return True

    def __hash__(self):
        """
        Hashes the puzzle configuration, used for comparing states in search algorithms.
        """
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
        Returns a string representation of the Fifteen Puzzle for display.
        """
        lines = []
        # /*=====End Change Task 1.6 =====*/
        # Adjust the horizontal line length for the 4x4 grid (since each tile takes 4 characters)
        horizontalLine = '-' * (4 * 4 + 1)  # 17 dashes for 4 columns and separators
        lines.append(horizontalLine)

        for row in self.cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '  # Display blank space for 0
                rowLine = rowLine + ' ' + str(col).rjust(2) + ' |'  # Right justify single-digit numbers
            lines.append(rowLine)
            lines.append(horizontalLine)
        # /*=====End Change Task 1.6 =====*/
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()


# The search problem for Fifteen Puzzle

class FifteenPuzzleSearchProblem(search.SearchProblem):
    """
    Implementation of a SearchProblem for the Fifteen Puzzle domain.

    Each state is represented by an instance of a FifteenPuzzleState.
    """

    def __init__(self, puzzle):
        """
        Creates a new FifteenPuzzleSearchProblem which stores the puzzle.
        """
        self.puzzle = puzzle  # Store the initial puzzle state

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.puzzle

    def isGoalState(self, state):
        """
        Returns True if the given state is the goal state.
        """
        return state.isGoal()

    def getSuccessors(self, state):
        """
        Returns a list of (successor, action, stepCost) tuples where each successor
        is the result of a legal move, and the cost is 1.0.
        """
        successors = []
        for action in state.legalMoves():
            nextState = state.result(action)
            successors.append((nextState, action, 1))
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the total cost of the given actions sequence (number of moves).
        """
        return len(actions)


# Helper functions

FIFTEEN_PUZZLE_DATA = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],  # Solved state
    [1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 9, 13, 14, 15],  # Nearly solved
]


def createRandomFifteenPuzzle(moves=100):
    """
    Creates a random fifteen puzzle by making the specified number of random moves from
    the solved state.
    """
    puzzle = FifteenPuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    for _ in range(moves):
        puzzle = puzzle.result(random.choice(puzzle.legalMoves()))
    return puzzle
from search import aStarSearch, h1_misplaced_tiles, h2_euclidean_distance, h3_manhattan_distance, h4_row_column_misplacements
if __name__ == '__main__':
    # Step 1: Generate a random 15-puzzle
    puzzle = createRandomFifteenPuzzle(25)
    print('A random 15-puzzle:')
    print(puzzle)

    # Step 2: Create the problem instance
    problem = FifteenPuzzleSearchProblem(puzzle)

    # Step 3: Prompt the user to select a heuristic
    print("\nChoose a heuristic:")
    print("1: h1 - Misplaced Tiles")
    print("2: h2 - Euclidean Distance")
    print("3: h3 - Manhattan Distance")
    print("4: h4 - Tiles out of Rows + Tiles out of Columns")

    heuristic_choice = input("Enter the number corresponding to your desired heuristic (1-4): ")

    # Step 4: Assign the heuristic based on the user's choice
    if heuristic_choice == '1':
        heuristic = h1_misplaced_tiles
        print("Using h1 - Misplaced Tiles heuristic")
    elif heuristic_choice == '2':
        heuristic = h2_euclidean_distance
        print("Using h2 - Euclidean Distance heuristic")
    elif heuristic_choice == '3':
        heuristic = h3_manhattan_distance
        print("Using h3 - Manhattan Distance heuristic")
    elif heuristic_choice == '4':
        heuristic = h4_row_column_misplacements
        print("Using h4 - Tiles out of Rows + Tiles out of Columns heuristic")
    else:
        print("Invalid input! Defaulting to h1 - Misplaced Tiles heuristic.")
        heuristic = h1_misplaced_tiles

    # Step 5: Solve the puzzle using A* with the chosen heuristic
    path = aStarSearch(problem, heuristic=heuristic)

    # Step 6: Output the solution
    print('A* found a path of %d moves: %s' % (len(path), str(path)))
    curr = puzzle
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i > 1], a))
        print(curr)
        input("Press return for the next state...")  # Wait for user input to proceed
        i += 1