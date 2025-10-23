#!/usr/bin/env python3
"""
Tests for puzzle implementations.
"""

import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from puzzles.fifteen_puzzle import FifteenPuzzleState, FifteenPuzzleSearchProblem
from puzzles.eight_puzzle import EightPuzzleState, EightPuzzleSearchProblem


class TestFifteenPuzzle(unittest.TestCase):
    """Test cases for Fifteen Puzzle implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Solved state
        self.solved_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.solved_puzzle = FifteenPuzzleState(self.solved_state)
        
        # Unsolved state
        self.unsolved_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
        self.unsolved_puzzle = FifteenPuzzleState(self.unsolved_state)
    
    def test_solved_state(self):
        """Test that solved state is recognized correctly."""
        self.assertTrue(self.solved_puzzle.isGoal())
        self.assertFalse(self.unsolved_puzzle.isGoal())
    
    def test_legal_moves(self):
        """Test legal moves generation."""
        # For solved state, blank is at bottom-right, so legal moves are 'up' and 'left'
        legal_moves = self.solved_puzzle.legalMoves()
        self.assertIn('up', legal_moves)
        self.assertIn('left', legal_moves)
        self.assertNotIn('down', legal_moves)
        self.assertNotIn('right', legal_moves)
    
    def test_move_result(self):
        """Test that moves produce correct results."""
        # Move blank up from solved state
        new_puzzle = self.solved_puzzle.result('up')
        self.assertEqual(new_puzzle.blankLocation, (3, 2))  # Should be at (3,2)
        
        # Move blank left from solved state
        new_puzzle = self.solved_puzzle.result('left')
        self.assertEqual(new_puzzle.blankLocation, (3, 2))  # Should be at (3,2)
    
    def test_puzzle_equality(self):
        """Test puzzle equality comparison."""
        puzzle1 = FifteenPuzzleState(self.solved_state)
        puzzle2 = FifteenPuzzleState(self.solved_state)
        puzzle3 = FifteenPuzzleState(self.unsolved_state)
        
        self.assertEqual(puzzle1, puzzle2)
        self.assertNotEqual(puzzle1, puzzle3)
    
    def test_search_problem(self):
        """Test search problem implementation."""
        problem = FifteenPuzzleSearchProblem(self.solved_puzzle)
        
        self.assertEqual(problem.getStartState(), self.solved_puzzle)
        self.assertTrue(problem.isGoalState(self.solved_puzzle))
        self.assertFalse(problem.isGoalState(self.unsolved_puzzle))
        
        successors = problem.getSuccessors(self.solved_puzzle)
        self.assertGreater(len(successors), 0)


class TestEightPuzzle(unittest.TestCase):
    """Test cases for Eight Puzzle implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Solved state
        self.solved_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.solved_puzzle = EightPuzzleState(self.solved_state)
        
        # Unsolved state
        self.unsolved_state = [1, 0, 2, 3, 4, 5, 6, 7, 8]
        self.unsolved_puzzle = EightPuzzleState(self.unsolved_state)
    
    def test_solved_state(self):
        """Test that solved state is recognized correctly."""
        self.assertTrue(self.solved_puzzle.isGoal())
        self.assertFalse(self.unsolved_puzzle.isGoal())
    
    def test_legal_moves(self):
        """Test legal moves generation."""
        # For solved state, blank is at top-left, so legal moves are 'down' and 'right'
        legal_moves = self.solved_puzzle.legalMoves()
        self.assertIn('down', legal_moves)
        self.assertIn('right', legal_moves)
        self.assertNotIn('up', legal_moves)
        self.assertNotIn('left', legal_moves)
    
    def test_move_result(self):
        """Test that moves produce correct results."""
        # Move blank down from solved state
        new_puzzle = self.solved_puzzle.result('down')
        self.assertEqual(new_puzzle.blankLocation, (1, 0))  # Should be at (1,0)
        
        # Move blank right from solved state
        new_puzzle = self.solved_puzzle.result('right')
        self.assertEqual(new_puzzle.blankLocation, (0, 1))  # Should be at (0,1)
    
    def test_search_problem(self):
        """Test search problem implementation."""
        problem = EightPuzzleSearchProblem(self.solved_puzzle)
        
        self.assertEqual(problem.getStartState(), self.solved_puzzle)
        self.assertTrue(problem.isGoalState(self.solved_puzzle))
        self.assertFalse(problem.isGoalState(self.unsolved_puzzle))


if __name__ == '__main__':
    unittest.main()
