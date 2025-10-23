#!/usr/bin/env python3
"""
Basic N-Puzzle Solver Example

This script demonstrates how to solve N-puzzles using different algorithms and heuristics.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from puzzles.fifteen_puzzle import FifteenPuzzleState, FifteenPuzzleSearchProblem
from algorithms.search import aStarSearch, breadthFirstSearch, depthFirstSearch, uniformCostSearch
from algorithms.heuristics import h1_misplaced_tiles, h2_euclidean_distance, h3_manhattan_distance, h4_row_column_misplacements


def solve_puzzle(puzzle_state, algorithm='astar', heuristic=None):
    """
    Solve a puzzle using the specified algorithm and heuristic.
    
    Args:
        puzzle_state: The initial puzzle state
        algorithm: The search algorithm to use ('astar', 'bfs', 'dfs', 'ucs')
        heuristic: The heuristic function to use (only for A*)
        
    Returns:
        tuple: (solution_path, expanded_nodes, max_fringe_size)
    """
    puzzle = FifteenPuzzleState(puzzle_state)
    problem = FifteenPuzzleSearchProblem(puzzle)
    
    if algorithm == 'astar':
        if heuristic is None:
            heuristic = h3_manhattan_distance  # Default to Manhattan distance
        solution = aStarSearch(problem, heuristic)
        return solution, 0, 0  # Simplified for basic example
    elif algorithm == 'bfs':
        solution, max_fringe, expanded = breadthFirstSearch(problem)
        return solution, expanded, max_fringe
    elif algorithm == 'dfs':
        solution, max_fringe, expanded = depthFirstSearch(problem)
        return solution, expanded, max_fringe
    elif algorithm == 'ucs':
        solution, max_fringe, expanded = uniformCostSearch(problem)
        return solution, expanded, max_fringe
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")


def main():
    """Main function to demonstrate puzzle solving."""
    
    # Example puzzle state (nearly solved)
    puzzle_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15]
    
    print("=== N-Puzzle Solver Demo ===")
    print(f"Initial puzzle state: {puzzle_state}")
    
    # Create puzzle object for display
    puzzle = FifteenPuzzleState(puzzle_state)
    print("\nInitial puzzle configuration:")
    print(puzzle)
    
    # Test different algorithms
    algorithms = [
        ('A* with Manhattan Distance', 'astar', h3_manhattan_distance),
        ('A* with Misplaced Tiles', 'astar', h1_misplaced_tiles),
        ('A* with Euclidean Distance', 'astar', h2_euclidean_distance),
        ('A* with Row-Column Misplacements', 'astar', h4_row_column_misplacements),
        ('Breadth-First Search', 'bfs', None),
        ('Depth-First Search', 'dfs', None),
        ('Uniform Cost Search', 'ucs', None)
    ]
    
    print("\n=== Solving with different algorithms ===")
    
    for name, algorithm, heuristic in algorithms:
        print(f"\n{name}:")
        try:
            solution, expanded, max_fringe = solve_puzzle(puzzle_state, algorithm, heuristic)
            if solution:
                print(f"  Solution found in {len(solution)} moves")
                print(f"  Solution path: {solution}")
                print(f"  Expanded nodes: {expanded}")
                print(f"  Max fringe size: {max_fringe}")
            else:
                print("  No solution found")
        except Exception as e:
            print(f"  Error: {e}")
    
    print("\n=== Interactive Demo ===")
    print("You can also try solving a random puzzle:")
    
    # Generate a random puzzle
    random_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
    random_puzzle_obj = FifteenPuzzleState(random_puzzle)
    print("\nRandom puzzle:")
    print(random_puzzle_obj)
    
    # Solve the random puzzle
    solution = solve_puzzle(random_puzzle, 'astar', h3_manhattan_distance)[0]
    if solution:
        print(f"\nSolution found in {len(solution)} moves: {solution}")
    else:
        print("\nNo solution found")


if __name__ == "__main__":
    main()
