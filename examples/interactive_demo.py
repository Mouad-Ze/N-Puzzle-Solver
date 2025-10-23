#!/usr/bin/env python3
"""
Interactive N-Puzzle Demo

This script provides an interactive interface for solving N-puzzles step by step.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from puzzles.fifteen_puzzle import FifteenPuzzleState, FifteenPuzzleSearchProblem
from algorithms.search import aStarSearch
from algorithms.heuristics import HEURISTICS


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("           N-Puzzle Interactive Solver")
    print("="*50)
    print("1. Solve a random puzzle")
    print("2. Solve a custom puzzle")
    print("3. Choose heuristic function")
    print("4. Step-by-step solution")
    print("5. Quick solve")
    print("0. Exit")
    print("="*50)


def display_heuristics():
    """Display available heuristics."""
    print("\nAvailable heuristics:")
    print("1. Manhattan Distance (recommended)")
    print("2. Misplaced Tiles")
    print("3. Euclidean Distance")
    print("4. Row-Column Misplacements")
    print("5. Null Heuristic (Uniform Cost)")


def get_heuristic_choice():
    """Get user's heuristic choice."""
    display_heuristics()
    while True:
        try:
            choice = int(input("\nSelect heuristic (1-5): "))
            if 1 <= choice <= 5:
                heuristic_names = [
                    'manhattan_distance',
                    'misplaced_tiles', 
                    'euclidean_distance',
                    'row_column_misplacements',
                    'null'
                ]
                return HEURISTICS[heuristic_names[choice - 1]]
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


def solve_random_puzzle(heuristic):
    """Solve a randomly generated puzzle."""
    print("\nGenerating random puzzle...")
    
    # Create a simple shuffled puzzle
    puzzle_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
    puzzle = FifteenPuzzleState(puzzle_state)
    
    print("\nRandom puzzle:")
    print(puzzle)
    
    return solve_puzzle(puzzle, heuristic)


def solve_custom_puzzle(heuristic):
    """Solve a user-provided puzzle."""
    print("\nEnter your puzzle state as a comma-separated list of 16 numbers (0-15).")
    print("Example: 1,2,3,4,5,6,7,8,9,10,11,12,13,0,14,15")
    
    while True:
        try:
            puzzle_input = input("\nPuzzle state: ")
            puzzle_state = [int(x.strip()) for x in puzzle_input.split(',')]
            
            if len(puzzle_state) != 16:
                print("Error: Puzzle must have exactly 16 numbers.")
                continue
                
            if set(puzzle_state) != set(range(16)):
                print("Error: Puzzle must contain numbers 0-15 exactly once.")
                continue
                
            puzzle = FifteenPuzzleState(puzzle_state)
            print("\nYour puzzle:")
            print(puzzle)
            
            return solve_puzzle(puzzle, heuristic)
            
        except ValueError:
            print("Error: Please enter valid numbers separated by commas.")
        except Exception as e:
            print(f"Error: {e}")


def solve_puzzle(puzzle, heuristic):
    """Solve a puzzle using A* search."""
    problem = FifteenPuzzleSearchProblem(puzzle)
    
    print(f"\nSolving with {heuristic.__name__} heuristic...")
    print("Please wait...")
    
    solution = aStarSearch(problem, heuristic)
    
    if solution:
        print(f"\nSolution found in {len(solution)} moves!")
        return solution
    else:
        print("\nNo solution found.")
        return None


def step_by_step_solution(puzzle, solution):
    """Display the solution step by step."""
    if not solution:
        print("No solution to display.")
        return
    
    print(f"\nShowing solution step by step ({len(solution)} moves):")
    print("Press Enter to see each move, or 'q' to quit...")
    
    current_puzzle = puzzle
    for i, move in enumerate(solution, 1):
        input(f"\nMove {i}: {move} (Press Enter to continue)")
        current_puzzle = current_puzzle.result(move)
        print(f"\nAfter move {i} ({move}):")
        print(current_puzzle)
    
    print("\nPuzzle solved! 🎉")


def quick_solve(puzzle, solution):
    """Display the solution quickly."""
    if not solution:
        print("No solution to display.")
        return
    
    print(f"\nQuick solution ({len(solution)} moves):")
    print("Solution path:", solution)
    
    # Show final result
    current_puzzle = puzzle
    for move in solution:
        current_puzzle = current_puzzle.result(move)
    
    print("\nFinal solved state:")
    print(current_puzzle)


def main():
    """Main interactive loop."""
    print("Welcome to the N-Puzzle Interactive Solver!")
    
    current_heuristic = HEURISTICS['manhattan_distance']
    current_solution = None
    current_puzzle = None
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nSelect an option (0-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 0:
            print("Thank you for using the N-Puzzle Solver!")
            break
        elif choice == 1:
            current_solution = solve_random_puzzle(current_heuristic)
            if current_solution:
                current_puzzle = FifteenPuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15])
        elif choice == 2:
            current_solution = solve_custom_puzzle(current_heuristic)
            if current_solution:
                current_puzzle = FifteenPuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15])
        elif choice == 3:
            current_heuristic = get_heuristic_choice()
            print(f"Heuristic changed to: {current_heuristic.__name__}")
        elif choice == 4:
            if current_solution and current_puzzle:
                step_by_step_solution(current_puzzle, current_solution)
            else:
                print("Please solve a puzzle first (options 1 or 2).")
        elif choice == 5:
            if current_solution and current_puzzle:
                quick_solve(current_puzzle, current_solution)
            else:
                print("Please solve a puzzle first (options 1 or 2).")
        else:
            print("Invalid choice. Please select 0-5.")


if __name__ == "__main__":
    main()
