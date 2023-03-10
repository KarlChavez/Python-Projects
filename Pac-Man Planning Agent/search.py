# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import heappush, heappop
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
      """
      Returns the start state for the search problem
      """
      util.raiseNotDefined()

    def isGoalState(self, state):
      """
      state: Search state

      Returns True if and only if the state is a valid goal state
      """
      util.raiseNotDefined()

    def getSuccessors(self, state):
      """
      state: Search state

      For a given state, this should return a list of triples,
      (successor, action, stepCost), where 'successor' is a
      successor to the current state, 'action' is the action
      required to get there, and 'stepCost' is the incremental
      cost of expanding to that successor
      """
      util.raiseNotDefined()

    def getCostOfActions(self, actions):
      """
      actions: A list of actions to take

      This method returns the total cost of a particular sequence of actions.  The sequence must
      be composed of legal moves
      """
      util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure that you implement the graph search version of DFS,
    which avoids expanding any already visited states. 
    Otherwise your implementation may run infinitely!
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """
    YOUR CODE HERE
    """
    stackDfs = util.Stack() 
    closedSet = set() 
    start = problem.getStartState() #Start node
    actions = [] #Actions taken from start to current state
    stackDfs.push((start, actions)) #Tuple

    while not stackDfs.isEmpty(): #Iterate until stack is empty
        state, actions = stackDfs.pop()

        if state in closedSet: #Iterate if it has been visited already
            continue 

        if problem.isGoalState(state): #Check if goal has been reached
            return actions

        closedSet.add(state) #State has been explored

        #Add successors onto stack and update actions
        for (next_state, action, cost) in problem.getSuccessors(state): 
            stackDfs.push((next_state, actions + [action]))

    #Return empty array if no goal state
    return [] 

def breadthFirstSearch(problem):
    queueBfs = util.Queue() 
    closedSet = set() 
    start = problem.getStartState() #Start node
    actions = [] #Actions taken from start to current state
    queueBfs.push((start, actions)) #Tuple

    while not queueBfs.isEmpty(): #Iterate until queue is empty
        state, actions = queueBfs.pop()

        if state in closedSet: #Iterate if it has been visited already
            continue 

        if problem.isGoalState(state): #Check if goal has been reached
            return actions

        closedSet.add(state) #State has been explored

        #Add successors onto queue and update actions
        for (next_state, action, cost) in problem.getSuccessors(state): 
            queueBfs.push((next_state, actions + [action]))
    
    #Return empty array if no goal state
    return []

def uniformCostSearch(problem):
    heapUcs = util.PriorityQueue()
    closedSet = set()
    start = problem.getStartState() #Start node
    actions = [] #Actions taken from start to current state
    heapUcs.push((start, actions), 0) #Tuple
    
    while not heapUcs.isEmpty(): #Iterate until heap is empty
        (state, actions) = heapUcs.pop()
        
        if state in closedSet: #Iterate if it has been visited already
            continue
        
        if problem.isGoalState(state): #Check if goal has been reached
            return actions
        
        closedSet.add(state) #State has been explored
        
        #Add successors onto heap and update actions
        for next_state, action, cost in problem.getSuccessors(state):
              #adding total cost
              totalCost = cost + problem.getCostOfActions(actions + [action])
              heapUcs.push((next_state, actions + [action]), totalCost)
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    YOUR CODE HERE
    """
    heapUcs = util.PriorityQueue()
    closedSet = set()
    start = problem.getStartState() #Start node
    actions = [] #Actions taken from start to current state
    heapUcs.push((start, [], 0), heuristic(start, problem)) #Tuple
    
    while not heapUcs.isEmpty(): #Iterate until heap is empty
        state, actions, costs = heapUcs.pop()
        
        if state in closedSet: #Iterate if it has been visited already
            continue
        
        if problem.isGoalState(state): #Check if goal has been reached
            return actions
        
        closedSet.add(state) #State has been explored
        
        #Add successors onto heap and update actions
        for next_state, action, cost in problem.getSuccessors(state):
              actionList = list(actions) + [action] 
              totalCost = problem.getCostOfActions(actionList)
              #Heuristic account in priority queue, not the actual tuple
              heapUcs.push((next_state, actionList, 1), totalCost + heuristic(next_state, problem))
    
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
