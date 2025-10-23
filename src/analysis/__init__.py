"""
Analysis tools for N-Puzzle Solver performance evaluation.
"""

from .automate import run_heuristic_comparison, analyze_results
from .task4 import run_strategic_comparison, analyze_result

__all__ = [
    'run_heuristic_comparison',
    'analyze_results',
    'run_strategic_comparison', 
    'analyze_result'
]
