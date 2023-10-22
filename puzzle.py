import copy

class PuzzleState:
    def __init__(self,twoDArray):
        self.matrix = twoDArray

    def __str__(self):
        str=''
        for i in range(3):
            str+='|'
            for j in range(3):
                str=f'{str}{self.matrix[i][j]}\t'
            str+='|\n'
        str += '\n\n'
        return str
    
    def next_States(self):
        states = []
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] is None:
                    break
            if self.matrix[i][j] is None:
                break
        
        if j<2:
            newState=copy.deepcopy(self)
            newState.matrix[i][j],newState.matrix[i][j+1]=newState.matrix[i][j+1],newState.matrix[i][j]
            states.append(newState)
        if j>0:
            newState=copy.deepcopy(self)
            newState.matrix[i][j],newState.matrix[i][j-1]=newState.matrix[i][j-1],newState.matrix[i][j]
            states.append(newState)

        if i<2:
            newState=copy.deepcopy(self)
            newState.matrix[i][j],newState.matrix[i+1][j]=newState.matrix[i+1][j],newState.matrix[i][j]
            states.append(newState)
        if i>0:
            newState=copy.deepcopy(self)
            newState.matrix[i][j],newState.matrix[i-1][j]=newState.matrix[i-1][j],newState.matrix[i][j]
            states.append(newState)
    
        return states
    
    def indiciesof(self,tile):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == tile:
                    return i,j
    
    def h(self,target):
        total = 0
        for tile in range(1,9):
            [i,j]=self.indiciesof(tile)
            [iTarget,jTarget]=target.indiciesof(tile)
            total += abs(i-iTarget)+abs(j-jTarget)
             
        return total
        

if __name__ == "__main__":
    
    startState=PuzzleState([[1,2,3],[4,None,6],[5,7,8]])
    #   1   2   3
    #   4       6
    #   5   7   8
    targetState=PuzzleState([[1,2,3],[4,5,6],[7,8,None]])
    #   1   2   3
    #   4   5   6
    #   7   8

    # states = startState.next_States()

    # print("current state:")
    # print(startState)
    # print("next states:")
    # for state in states:
    #     print(state)

    # print(startState.h(targetState))

    