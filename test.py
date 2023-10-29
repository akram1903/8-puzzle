import copy
import puzzle
from heapdict import *
# s = { 1,2,3}

# print(s)

# s.add(4)
# s.add("aan")
# print(s)

# if "aan" in s:
#     print(f"aan in {s}")


m=puzzle.PuzzleState([[1,2,3],[4,None,6],[5,7,8]])

mcopy = copy.deepcopy(m)

frontier = heapdict()

frontier[m]=m.level
frontier[mcopy]=mcopy.level

print(set(frontier.keys()))