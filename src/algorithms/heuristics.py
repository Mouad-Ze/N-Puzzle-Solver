# heuristics.py
# ------------
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

"""
Heuristic functions for N-Puzzle solving algorithms.
These functions estimate the cost from the current state to the goal state.
"""

import math


def null_heuristic(state, problem=None):
    """
    A trivial heuristic function that always returns 0.
    This is equivalent to uniform cost search.
    """
    return 0


def h1_misplaced_tiles(state, problem=None):
    """
    Heuristic 1: Misplaced Tiles
    Counts the number of tiles that are not in the correct position.
    """
    misplaced = 0
    goal = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]]

    for i in range(4):
        for j in range(4):
            if state.cells[i][j] != 0 and state.cells[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced


def h2_euclidean_distance(state, problem=None):
    """
    Heuristic 2: Euclidean Distance
    Calculates the sum of Euclidean distances from each tile's current 
    position to its goal position.
    """
    total_distance = 0
    for i in range(4):
        for j in range(4):
            tile = state.cells[i][j]
            if tile != 0:
                goal_row, goal_col = divmod(tile - 1, 4)
                total_distance += math.sqrt((goal_row - i) ** 2 + (goal_col - j) ** 2)
    return total_distance


def h3_manhattan_distance(state, problem=None):
    """
    Heuristic 3: Manhattan Distance
    Calculates the sum of Manhattan distances from each tile's current 
    position to its goal position.
    This is the most commonly used heuristic for N-puzzle problems.
    """
    total_distance = 0
    for i in range(4):
        for j in range(4):
            tile = state.cells[i][j]
            if tile != 0:
                goal_row, goal_col = divmod(tile - 1, 4)
                total_distance += abs(goal_row - i) + abs(goal_col - j)
    return total_distance


def h4_row_column_misplacements(state, problem=None):
    """
    Heuristic 4: Row-Column Misplacements
    Sums the number of tiles that are out of their correct row and column.
    """
    row_misplaced = 0
    col_misplaced = 0
    for i in range(4):
        for j in range(4):
            tile = state.cells[i][j]
            if tile != 0:
                goal_row, goal_col = divmod(tile - 1, 4)
                if i != goal_row:
                    row_misplaced += 1
                if j != goal_col:
                    col_misplaced += 1
    return row_misplaced + col_misplaced


# Dictionary of available heuristics for easy access
HEURISTICS = {
    'null': null_heuristic,
    'misplaced_tiles': h1_misplaced_tiles,
    'euclidean_distance': h2_euclidean_distance,
    'manhattan_distance': h3_manhattan_distance,
    'row_column_misplacements': h4_row_column_misplacements
}


def get_heuristic(name):
    """
    Get a heuristic function by name.
    
    Args:
        name (str): Name of the heuristic
        
    Returns:
        function: The heuristic function
        
    Raises:
        ValueError: If the heuristic name is not found
    """
    if name not in HEURISTICS:
        raise ValueError(f"Unknown heuristic: {name}. Available heuristics: {list(HEURISTICS.keys())}")
    return HEURISTICS[name]
