"""
Puzzle implementations for N-Puzzle Solver.
"""

from .eight_puzzle import EightPuzzleState, EightPuzzleSearchProblem
from .fifteen_puzzle import FifteenPuzzleState, FifteenPuzzleSearchProblem

__all__ = [
    'EightPuzzleState',
    'EightPuzzleSearchProblem', 
    'FifteenPuzzleState',
    'FifteenPuzzleSearchProblem'
]
