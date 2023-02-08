In this homework, you are to implement four search algorithms --- DFS, BFS, UCS, and A* --- in search.py so that a pacman planning agent can complete the search problem. You are to implement the "graph" search rather than the "tree" search version.

Download  hw1_template.zip from Carmen and unpack it. This code, and the idea for the assignment, comes from UC Berkeley Links to an external site..

Open up the Windows Command Line or Mac Terminal or Linux Terminal.

Change your directory to the folder with the pacman code. You should see a file called commands.txt and four folders: py, layouts, test_cases and images.

Run some of these commands (as listed in commands.txt) to make sure your setup works. Below are some examples:

python3 py/pacman.py
python3 py/pacman.py --layout tinyMaze --pacman GoWestAgent
Make sure you can execute the above. You will not be able to complete the assignment if your environment does not allow you to run the above commands.
Possible errors and notes
If you're unable to run pacman.py or get its graphics to work, or if you're getting an error about "tkinter" or "_tkinter", that's okay. As long as you can run autograder.py, you should be able to complete the assignment fully.

We note that, the provided commands are designed to work with Mac/Linux with Python version 3. If you use Windows (like me!), we recommend that you run the code in the Windows command line (CMD), and make the following changes:

Please use \ instead of / while specifying the path to the file. (This isn't strictly necessary, Windows will accept both.)
If it still does not work, you may use py -3 instead of python3 in the command you're executing on CMD. An example command that works for us is py -3 py\autograder.py.
We suggest that you run the code on Command Line. You may use editors like PyCharm to write your code.
Implementation (in search.py)
Please use python3 and write your own solutions from scratch. Do not import any packages yourself except for those we have included and specified.

Please only implement your code at where we indicate.

Please implement the "graph" search version, not the tree search version of each algorithm. That is, you will create a closed-set, and you will not expand the already expanded states again.

In defining the close-set, please simply create a "set" (not a "list") and insert visited/expanded states into the close-set by yourself. There is a "self.expanded" variable in searchagent.py, but we highly suggest that you do NOT use that variable since our grading script may not check it.

Once you finish your implementation, you can execute the autograder by

python3 py/autograder.py
The full grade shown in the autograder is 35, while the full grade of your programming part is 50.

Please also read Other information at the end of this page for some other hints.

Task 1 (12.5 pts): Depth-First Search (DFS)
Open the file py/search.py and find the function depthFirstSearch.

Take the provided template and finish the code (at "YOUR CODE HERE") so that depth-first search works. To do so, please first check the class SearchProblem. This class outlines the structure of a search problem. It provides functions like getStartState, isGoalState (i.e., goal test), getSuccessors, and getCostOfActions. In your implementation, you will be using these functions to get necessary information about the search problem. Please note that, this is a abstract class that we put here to help you understand a search problem. The detail of the class is implemented in some other .py files by us already.

We suggest that you put the successors into the fringe in either the right-to-left or left-to-right fashion, not the others.

You can test it with pacman by running the following command:

python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
Task 2 (12.5 pts): Breadth-First Search (BFS)
Open the file py/search.py and and find the function breadthFirstSearch.

Take the template and finish the BFS alorithm (at "YOUR CODE HERE"). We suggest that you put the successors into the fringe in either the right-to-left or left-to-right fashion, not the others.

You can test it with pacman by running the following command:

python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
(Note that this should be simple if you've completed Task 1.)

Task 3 (12.5 pts): Uniform Cost Search (UCS)
Open the file py/search.py and find the function uniformCostSearch.

Take the template and finish the code (at "YOUR CODE HERE") so that UCS works.

You can test it with pacman by running the following command:

python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
(Note that adapting your implementation of DFS or BFS maybe useful for UCS.)

Useful Python code
Task 3 above asks you to implement UCS for Pacman. So, you want to have an open-set that's ordered by the accumulated cost. You may use heaps for this purpose. Whenever you pop a value from a heap, the lowest value comes out. Use a tuple to keep the value and other data together. For example:

from util import heappush, heappop
openset = []
heappush(openset, (5, "foo"))
heappush(openset, (7, "bar"))
heappush(openset, (3, "baz"))
heappush(openset, (9, "quux"))
best = heappop(openset)
print(best)
Alternatively, you can use the PriorityQueue data structures provided to you in py/util.py!

Task 4 (12.5 pts): A* Search
Open the file py/search.py and find the function aStarSearch.

Finish the implementation of A* search (at "YOUR CODE HERE"). You can use the argument heuristic as a function: dist = heuristic(state, problem). That is, try h_start = heuristic(problem.getStartState(), problem); print(h_start). The class nullHeuristic outlines the input and output of a heuristic function. We have implemented the heuristic functions.

You can test it with pacman by running the following command:

python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
