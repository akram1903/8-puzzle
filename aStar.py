import puzzle
from queue import PriorityQueue


class Tree:
    def __init__(self,rootNodeState,targetState):
        self.root = rootNodeState
        self.target = targetState

    def aStarTraverse(self):
        
        # frontier is the queue 
        frontier = PriorityQueue()
        frontier.put((self.root.h(),self.root))

        # explored is the set of all visited nodes
        explored = set()
        
        while not frontier.empty:
            currentState=frontier.get()
            explored.add(currentState)

            if currentState == self.target:
                return currentState
            # returning the final target then a function takes that output and make an array for the path
            # that function is not done
            
            neighbors = currentState.nextStates()

            for neighbor in neighbors:
                if neighbor not in frontier and neighbor not in explored:
                    frontier.put((neighbor.h()+neighbor.g,neighbor))
                elif neighbor in frontier:
                    frontier.
                    # to be continued

        return None





startState=puzzle.PuzzleState([[1,2,3],[4,None,6],[5,7,8]])
#   1   2   3
#   4       6
#   5   7   8
targetState=puzzle.PuzzleState([[1,2,3],[4,5,6],[7,8,None]])
#   1   2   3
#   4   5   6
#   7   8

states = startState.nextStates()

# print("current state:")
# print(startState)
# print("next states:")
# for state in states:
#     print(state)