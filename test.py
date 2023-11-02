# import copy
# import puzzle
# from heapdict import *
# # s = { 1,2,3}

# # print(s)

# # s.add(4)
# # s.add("aan")
# # print(s)

# # if "aan" in s:
# #     print(f"aan in {s}")


# m=puzzle.PuzzleState([[1,2,3],[4,None,6],[5,7,8]])

# mcopy = copy.deepcopy(m)

# frontier = heapdict()

# frontier[m]=m.level
# frontier[mcopy]=mcopy.level

# print(set(frontier.keys()))


# import networkx as nx

# g = nx.Graph()
# g.add_node(1)
# g.add_node("hello")
# g.add_node(2)
# g.add_node(3)

# g.add_edges_from([(1,2),("hello",1)])
# print(g.graph)

