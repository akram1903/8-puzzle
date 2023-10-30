import copy
import math

class PuzzleState: # carries the state representation + tree's node children and parent
    # if it's the start case don't enter parent parameter else
    def __init__(self,twoDArray,children=[],parent=None):
        self.matrix = twoDArray
        self.children=children
        self.parent = parent
        self.heuristic = None
        if parent is not None:
            self.level = 1+self.parent.g
        else:
            self.level = 0

    def __hash__(self) -> int:
        result = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] is not None:
                    result+= self.matrix[i][j]*(10**(j+i*3))
        return result
    
    def __str__(self):
        str=''
        for i in range(3):
            str+='|'
            for j in range(3):
                str=f'{str}{self.matrix[i][j]}\t'
            str+='|\n'
        str += '\n\n'
        return str
    
    def nextStates(self):
        states = []
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] is None:
                    break
            if self.matrix[i][j] is None:
                break
        
        if j<2:
            newState=copy.deepcopy(self)
            newState.level = self.level+1
            newState.parent = self
            newState.matrix[i][j],newState.matrix[i][j+1]=newState.matrix[i][j+1],newState.matrix[i][j]
            states.append(newState)
        if j>0:
            newState=copy.deepcopy(self)
            newState.level = self.level+1
            newState.parent = self
            newState.matrix[i][j],newState.matrix[i][j-1]=newState.matrix[i][j-1],newState.matrix[i][j]
            states.append(newState)

        if i<2:
            newState=copy.deepcopy(self)
            newState.level = self.level+1
            newState.parent = self
            newState.matrix[i][j],newState.matrix[i+1][j]=newState.matrix[i+1][j],newState.matrix[i][j]
            states.append(newState)
        if i>0:
            newState=copy.deepcopy(self)
            newState.level = self.level+1
            newState.parent = self
            newState.matrix[i][j],newState.matrix[i-1][j]=newState.matrix[i-1][j],newState.matrix[i][j]
            states.append(newState)
    
        return states
    

    def h(self,target,flag='M'):
        total = 0
        for tile in range(1,9):
            [i,j]=self.indiciesof(tile)
            [iTarget,jTarget]=target.indiciesof(tile)
            if flag == 'M':
                total += manhattanDistance(i,iTarget,j,jTarget)
            else:
                total += euclideanDistance(i,iTarget,j,jTarget)
        
        self.heuristic = total
        return total
    def indiciesof(self,tile):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == tile:
                    return i,j
    
    
    
        
def manhattanDistance(i,it,j,jt):
        return abs(i-it)+abs(j-jt)
        
def euclideanDistance(i,it,j,jt):
    return math.sqrt((i-it)**2 + (j-jt)**2)

if __name__ == "__main__":
    
    startState=PuzzleState([[1,2,3],[4,None,6],[5,7,8]])
    #   1   2   3
    #   4       6
    #   5   7   8
    targetState=PuzzleState([[1,2,3],[4,5,6],[7,8,None]])
    #   1   2   3
    #   4   5   6
    #   7   8

    states = startState.nextStates()

    print("current state:")
    print(startState)
    print("next states:")
    for state in states:
        print(state)

    print(startState.h(targetState))

    