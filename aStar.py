import puzzle
import math


def manhattanDistance(i,it,j,jt):
        return abs(i-it)+abs(j-jt)
    
def euclideanDistance(i,it,j,jt):
    return math.sqrt((i-it)**2 + (j-jt)**2)

def h(self,target,flag='M'):
    total = 0
    for tile in range(1,9):
        [i,j]=self.indiciesof(tile)
        [iTarget,jTarget]=target.indiciesof(tile)
        if flag == 'M':
            total += manhattanDistance(i,iTarget,j,jTarget)
        else:
            total += euclideanDistance(i,iTarget,j,jTarget)

    return total


# startState=puzzle.PuzzleState([[1,2,3],[4,None,6],[5,7,8]])
# #   1   2   3
# #   4       6
# #   5   7   8
# targetState=puzzle.PuzzleState([[1,2,3],[4,5,6],[7,8,None]])
# #   1   2   3
# #   4   5   6
# #   7   8

# # states = startState.next_States()

# # print("current state:")
# # print(startState)
# # print("next states:")
# # for state in states:
# #     print(state)