# search.py
# ---------
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
In search.py, we implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# =====Start Change Task 2 & 3 & 4=====
def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""

    # states to be explored (LIFO). holds nodes in form (state, action)
    frontier = util.Stack()
    # previously explored states (for path checking), holds states
    exploredNodes = []

    max_depth = 10  # Set a maximum depth to prevent infinite loops

    maxFringeSize = 0
    nodesExpanded = 0
    # define start node
    startState = problem.getStartState()
    startNode = (startState, [],0)

    frontier.push(startNode)

    while not frontier.isEmpty():
        maxFringeSize = max(maxFringeSize, len(frontier.list))
        # begin exploring last (most-recently-pushed) node on frontier
        currentState, actions, current_depth = frontier.pop()
        nodesExpanded += 1

        if currentState not in exploredNodes:
            # mark current node as explored
            exploredNodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions, maxFringeSize, nodesExpanded
            else:
                # get list of possible successor nodes in
                # form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)

                # push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    new_depth = current_depth + 1
                    newNode = (succState, newAction,new_depth)

                    # Prevent exceeding the maximum depth
                    if new_depth <= max_depth:
                        frontier.push(newNode)



    return [], maxFringeSize, nodesExpanded


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # to be explored (FIFO)
    frontier = util.Queue()

    # previously expanded states (for cycle checking), holds states
    exploredNodes = []

    maxFringeSize = 0
    nodesExpanded = 0

    startState = problem.getStartState()
    startNode = (startState, [], 0)  # (state, action, cost)

    frontier.push(startNode)

    while not frontier.isEmpty():

        maxFringeSize = max(maxFringeSize, len(frontier.list))
        # begin exploring first (earliest-pushed) node on frontier
        currentState, actions, currentCost = frontier.pop()
        nodesExpanded += 1

        if currentState not in exploredNodes:
            # put popped node state into explored list
            exploredNodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions, maxFringeSize, nodesExpanded
            else:
                # list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)

                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.push(newNode)

    return [], maxFringeSize, nodesExpanded


        
def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    #to be explored (FIFO): holds (item, cost)
    frontier = util.PriorityQueue()

    #previously expanded states (for cycle checking), holds state:cost
    exploredNodes = {}

    maxFringeSize = 0
    nodesExpanded = 0
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode, 0)
    
    while not frontier.isEmpty():
        maxFringeSize = max(maxFringeSize, len(frontier.heap))
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
        nodesExpanded += 1

        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            #put popped node's state into explored list
            exploredNodes[currentState] = currentCost

            if problem.isGoalState(currentState):
                return actions, maxFringeSize, nodesExpanded
            else:
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:

                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.update(newNode, newCost)

    return [], maxFringeSize, nodesExpanded

# search.py

def h1_misplaced_tiles(state, problem=None):
    """Counts the number of tiles that are not in the correct position."""
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
    """Calculates the sum of Euclidean distances from each tile's current position to its goal position."""
    import math
    total_distance = 0
    for i in range(4):
        for j in range(4):
            tile = state.cells[i][j]
            if tile != 0:
                goal_row, goal_col = divmod(tile - 1, 4)
                total_distance += math.sqrt((goal_row - i) ** 2 + (goal_col - j) ** 2)
    return total_distance


def h3_manhattan_distance(state, problem=None):
    """Calculates the sum of Manhattan distances from each tile's current position to its goal position."""
    total_distance = 0
    for i in range(4):
        for j in range(4):
            tile = state.cells[i][j]
            if tile != 0:
                goal_row, goal_col = divmod(tile - 1, 4)
                total_distance += abs(goal_row - i) + abs(goal_col - j)
    return total_distance


def h4_row_column_misplacements(state, problem=None):
    """Sums the number of tiles that are out of their correct row and column."""
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


def aStarSearch(problem, heuristic=nullHeuristic, track_fringe=None, track_expansion=None):
    """
        A* Search algorithm that uses a heuristic function to guide the search.
    """
    fringe = util.PriorityQueue()

    exploredNodes = []  # Holds explored states along with the cost

    startState = problem.getStartState()
    startNode = (startState, [], 0)  # Initial state, no actions, zero cost

    fringe.push(startNode, heuristic(startState, problem))

    while not fringe.isEmpty():
        if track_fringe:
            track_fringe(fringe)  # Track fringe size

        currentState, actions, currentCost = fringe.pop()

        if problem.isGoalState(currentState):
            return actions

        exploredNodes.append((currentState, currentCost))

        if track_expansion:
            track_expansion()  # Track expanded nodes

        successors = problem.getSuccessors(currentState)

        for succState, succAction, succCost in successors:
            newActions = actions + [succAction]
            newCost = currentCost + succCost
            newNode = (succState, newActions, newCost)

            already_explored = False
            for exploredState, exploredCost in exploredNodes:
                if succState == exploredState and newCost >= exploredCost:
                    already_explored = True
                    break

            if not already_explored:
                priority = newCost + heuristic(succState, problem)
                fringe.push(newNode, priority)

    return []  # Return an empty path if no solution is found

# =====End Change Task 2 & 3 & 4=====

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
