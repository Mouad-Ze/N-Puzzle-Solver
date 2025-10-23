# N-Puzzle Solver

A comprehensive implementation of N-Puzzle solving algorithms using various search strategies and heuristics. This project includes implementations for both 8-puzzle (3x3) and 15-puzzle (4x4) variants.

## Features

### Search Algorithms
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Uniform Cost Search (UCS)**
- **A* Search Algorithm**

### Heuristic Functions for A* Search
- **h1**: Misplaced Tiles Heuristic
- **h2**: Euclidean Distance Heuristic
- **h3**: Manhattan Distance Heuristic
- **h4**: Row-Column Misplacements Heuristic

### Puzzle Variants
- **8-Puzzle**: 3x3 grid with 8 tiles and 1 blank space
- **15-Puzzle**: 4x4 grid with 15 tiles and 1 blank space

## Project Structure

```
n-puzzle-solver/
├── src/
│   ├── puzzles/
│   │   ├── eight_puzzle.py      # 8-puzzle implementation
│   │   └── fifteen_puzzle.py    # 15-puzzle implementation
│   ├── algorithms/
│   │   ├── search.py            # Core search algorithms
│   │   └── heuristics.py        # Heuristic functions
│   ├── utils/
│   │   ├── util.py              # Utility classes and data structures
│   │   └── generator.py         # Puzzle generation utilities
│   └── analysis/
│       ├── automate.py          # Heuristic comparison analysis
│       └── task4.py             # Strategy comparison analysis
├── examples/
│   ├── basic_solver.py          # Basic puzzle solving example
│   ├── heuristic_comparison.py  # Compare different heuristics
│   └── interactive_demo.py      # Interactive puzzle solver
├── tests/
│   ├── test_search.py           # Search algorithm tests
│   └── test_puzzles.py          # Puzzle implementation tests
├── data/
│   └── scenarios.csv            # Generated puzzle scenarios
├── results/
│   ├── heuristic_results.csv    # Heuristic comparison results
│   └── strategy_results.csv     # Strategy comparison results
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mouad-Ze/N-Puzzle-Solver.git
cd N-Puzzle-Solver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Puzzle Solving

```python
from src.puzzles.fifteen_puzzle import FifteenPuzzleState, FifteenPuzzleSearchProblem
from src.algorithms.search import aStarSearch, h3_manhattan_distance

# Create a random puzzle
puzzle = FifteenPuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
problem = FifteenPuzzleSearchProblem(puzzle)

# Solve using A* with Manhattan distance heuristic
solution = aStarSearch(problem, h3_manhattan_distance)
print(f"Solution found in {len(solution)} moves: {solution}")
```

### Interactive Demo

Run the interactive demo to solve puzzles step by step:

```bash
python examples/interactive_demo.py
```

### Heuristic Comparison

Compare the performance of different heuristics:

```bash
python examples/heuristic_comparison.py
```

### Strategy Analysis

Analyze different search strategies:

```bash
python src/analysis/automate.py
```

## Algorithm Details

### Search Algorithms

1. **Depth-First Search (DFS)**: Explores the deepest nodes first using a stack
2. **Breadth-First Search (BFS)**: Explores the shallowest nodes first using a queue
3. **Uniform Cost Search (UCS)**: Explores nodes with lowest path cost first using a priority queue
4. **A* Search**: Uses a heuristic function to guide the search toward the goal

### Heuristic Functions

1. **Misplaced Tiles (h1)**: Counts tiles not in their goal positions
2. **Euclidean Distance (h2)**: Sum of Euclidean distances from current to goal positions
3. **Manhattan Distance (h3)**: Sum of Manhattan distances from current to goal positions
4. **Row-Column Misplacements (h4)**: Counts tiles in wrong rows plus tiles in wrong columns

## Performance Analysis

The project includes comprehensive analysis tools to compare:
- **Nodes Expanded**: Number of nodes explored during search
- **Execution Time**: Time taken to find a solution
- **Maximum Fringe Size**: Peak memory usage during search
- **Solution Depth**: Length of the optimal solution path

## Results

Run the analysis scripts to generate performance comparisons:

```bash
# Compare heuristics
python src/analysis/automate.py

# Compare search strategies
python src/analysis/task4.py
```

Results are saved in the `results/` directory as CSV files for further analysis.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Acknowledgments

- Based on UC Berkeley's AI course materials
- Original implementations by John DeNero and Dan Klein
- Student implementations and enhancements by various contributors
