from puzzle import *
from heapdict import *


class Tree:
    def __init__(self,rootNodeState:PuzzleState,targetState:PuzzleState):
        self.root = rootNodeState
        self.target = targetState

    def aStarTraverse(self):
        # frontier is the queue of matrices 
        frontier = heapdict()
        frontier[self.root]=self.root.h(self.target)
        # frontierDict is to hold frontier States with matrix as key
        # frontierDict = {self.root.matrix : self.root}
        # explored is the set of all visited nodes matrices
        explored = set()
        
        while frontier.__len__() > 0:
            (currentState,notUsed)=frontier.popitem()
            # currentState =frontierDict[currentMatrix]
            explored.add(currentState.__hash__())
            
            print("________States explored________")
            print(currentState)
            
            if currentState.matrix == self.target.matrix:
                print("=========== final State ==========")
                return currentState
            # returning the final target then a function takes that output and make an array for the path
            
            neighbors = currentState.nextStates()

            for neighbor in neighbors:
                # print("##############__neighbors__##############")
                if neighbor.__hash__() not in set(frontier.keys()) and neighbor.__hash__() not in explored:
                    frontier[neighbor]=neighbor.h(self.target)+neighbor.level
                elif neighbor.__hash__() in frontier:
                    cost = neighbor.h(self.target)+neighbor.level
                    if frontier[neighbor]> cost:
                        frontier[neighbor]= cost
                        # print("---------decrease key ---------")
                        # print(neighbor)
                    

        return None




if __name__ == '__main__':
    startState=PuzzleState([
        [1,      2          ,5],
        [3,      4          ,8],
        [6,      None       ,7]])

    targetState=PuzzleState([
        [None,   1    ,2],
        [3,      4    ,5],
        [6,      7    ,8]])


    solutionClass = Tree(startState,targetState)
    solution = solutionClass.aStarTraverse()
    print(solution)
    # print("current state:")
    # print(startState)
    # print("next states:")
    # for state in states:
    #     print(state)