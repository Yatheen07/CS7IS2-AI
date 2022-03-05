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
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
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

def depthFirstSearch(problem):
    """Solution to Q1"""
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    #Create a stack to implement DFS and array to track visited nodes 
    nodesToExplore = []
    visitedNodes = []

    #Add the start state to the frontier
    start_state = problem.getStartState()
    nodesToExplore.append((start_state,[]))
    
    while len(nodesToExplore) > 0:
        #Get the node on top of stack from nodes to explore
        currentNode,goal_path = nodesToExplore.pop()

        #Goal Test
        if problem.isGoalState(currentNode):
            return goal_path
        
        #Add successors to stack
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            successors = problem.getSuccessors(currentNode)
            for successor in successors:
                new_goal_path = goal_path + [successor[1]]
                nodesToExplore.append((successor[0],new_goal_path))

    print("No Solution")
    return []

def breadthFirstSearch(problem):
    """Solution to Q2"""
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Create a stack to implement DFS and array to track visited nodes 
    nodesToExplore = []
    visitedNodes = []

    #Add the start state to the frontier
    start_state = problem.getStartState()
    nodesToExplore.append((start_state,[]))
    
    while len(nodesToExplore) > 0:
        #Get the node on top of stack from nodes to explore
        currentNode,goal_path = nodesToExplore[0]
        nodesToExplore = nodesToExplore[1:]

        #Goal Test
        if problem.isGoalState(currentNode):
            return goal_path
        
        #Add successors to stack
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            successors = problem.getSuccessors(currentNode)
            for successor in successors:
                new_goal_path = goal_path + [successor[1]]
                nodesToExplore.append((successor[0],new_goal_path))

    print("No Solution")
    return []

def uniformCostSearch(problem):

    """Solution to Q3"""
    """Search the node of least total cost first."""
    nodesToExplore = util.PriorityQueue()
    visitedNodes = []

    #Add the start state to the frontier
    start_state = (problem.getStartState(),[],0)
    nodesToExplore.update(start_state,0)

    while not nodesToExplore.isEmpty():
        #Get the node on top of stack from nodes to explore
        currentNode,goal_path,cost = nodesToExplore.pop()

        #Goal Test
        if problem.isGoalState(currentNode):
            return goal_path

        #Add successors to stack
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            successors = problem.getSuccessors(currentNode)
            for successor in successors:
                new_goal_path = goal_path + [successor[1]]
                new_cost = cost + successor[2]
                new_node = (successor[0],new_goal_path,new_cost)
                nodesToExplore.update(new_node,new_cost)

    print("No Solution")
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Solution to Q4"""
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    nodesToExplore = util.PriorityQueue()
    visitedNodes = []

    #Add the start state to the frontier
    start_state = (problem.getStartState(),[],0)
    nodesToExplore.push(start_state,0)

    #distance_matrix
    distance = {problem.getStartState() : 0}

    while not nodesToExplore.isEmpty():
        #Get the node on top of stack from nodes to explore
        currentNode,goal_path,path_cost = nodesToExplore.pop()
        path_cost = distance[currentNode]

        #Goal Test
        if problem.isGoalState(currentNode):
            return goal_path

        #Add successors to stack
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            successors = problem.getSuccessors(currentNode)
            for successor in successors:
                if successor not in visitedNodes:
                    successorNode,action, stepCost = successor[0],successor[1],successor[2]
                    
                    new_goal_path = goal_path + [action]
                    new_cost = path_cost + stepCost + heuristic(successorNode,problem)
                    new_node = (successorNode,new_goal_path,new_cost)

                    if successorNode in distance and distance[successorNode] < stepCost + path_cost:
                        continue

                    if successorNode in distance:
                        print("inhere")
                        nodesToExplore.update(new_node, stepCost + path_cost + heuristic(successorNode, problem))
                    else:
                        nodesToExplore.push(new_node, stepCost + path_cost + heuristic(successorNode, problem))
                    
                    distance[successorNode] = path_cost + stepCost

    print("No Solution")
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
