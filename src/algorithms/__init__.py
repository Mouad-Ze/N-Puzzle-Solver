"""
Search algorithms and heuristics for N-Puzzle Solver.
"""

from .search import (
    SearchProblem,
    depthFirstSearch,
    breadthFirstSearch,
    uniformCostSearch,
    aStarSearch
)

from .heuristics import (
    null_heuristic,
    h1_misplaced_tiles,
    h2_euclidean_distance,
    h3_manhattan_distance,
    h4_row_column_misplacements,
    HEURISTICS,
    get_heuristic
)

__all__ = [
    'SearchProblem',
    'depthFirstSearch',
    'breadthFirstSearch', 
    'uniformCostSearch',
    'aStarSearch',
    'null_heuristic',
    'h1_misplaced_tiles',
    'h2_euclidean_distance',
    'h3_manhattan_distance',
    'h4_row_column_misplacements',
    'HEURISTICS',
    'get_heuristic'
]
