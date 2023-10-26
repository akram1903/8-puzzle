import PuzzleState
class dDFS:
    def __init__(self,PuzzleState):
        self.puzzle = PuzzleState
    visited = [False ]
    stack =[]
    stack.append(puzzle)
    while (len(stack)):
        s = stack[-1]
        stack.pop()


        if(not visited[s])