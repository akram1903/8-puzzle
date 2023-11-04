#import math
import copy
import time
from queue import Queue 
      
      # This variable can be changed to change  the program from 8 puzzle(n=3) to 15  puzzle(n=4) to 24 puzzle(n=5)...
n = 3
#top, bottom, left, right
row = [-1, 1, 0, 0 ]
col = [ 0,0, -1, 1 ]
class node:


     def __init__(self, parent, matrix, empty_tile_pos,  cost, level):  
           # This will store the parent node to the  current node And helps in tracing the  path when the solution is visible  
          self.parent = parent  
          
          # Stores the matrix
          self.matrix = matrix
          
          # useful for Storing the position where the   empty space tile is already existing in the matrix  
          self.empty_tile_pos = empty_tile_pos
          
          # Store no. of misplaced tiles  
          self.cost = cost
  
          # Store no. of moves so far  
          self.level= level
     def __repr__(self):  
        return "Parent:% s Matrix:% s emptyPosition:% s costs:% s level:% s" % (self.parent, self.matrix, self.empty_tile_pos, self.costs ,self.level)  
        
        
def newNode(matrix, empty_tile_pos, new_empty_tile_pos,
            level, parent, cost,final) -> node:
                 
    # Copy data from parent matrix to current matrix
    new_mat = copy.deepcopy(matrix)
 
    # Move tile by 1 position
    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
 
    # Set number of misplaced tiles
#     cost = calculateCost(new_mat, final)
 
    new_node = node(parent, new_mat, new_empty_tile_pos,
                    cost, level)
    return new_node
     
     
          # Function to check if (x, y) is a valid matrix coordinate
def isSafe(x, y):
               
          return(( x >= 0 and x < n) and (y >= 0 and y < n))
     # Function to print the N x N matrix
# Function to print the N x N matrix
def printMatrix(mat):
     print(mat)
#     for i in range(n):
#         for j in range(n):
#             print("%d " % (mat[i][j]), end = " ")
             
#         print()
     
          # Print path from root node to destination node
def printPath(root):
     
    if root == None:
        return
     
    printPath(root.parent)
    printMatrix(root.matrix)
    print()
# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
    inv_count = 0
    empty_value = None
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    print("Inversion Count:",inv_count)
    return inv_count
     
# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)
 
     
 
 
     # Function to solve N*N - 1 puzzle algorithm using Branch and Bound. empty_tile_pos is the blank tile position in the initial state.
def solve_BFS(initial, empty_tile_pos, final):
     start_time = time.time()
     if(isSolvable(initial)) :
               print("Solvable")
          # Start timer
                    #       Queue for frontier states
               frontier=Queue()
               frontier_Set=set()
               # Create the root node
     #cost = calculateCost(initial, final)
               root = node(None, initial,  empty_tile_pos, 0, 0)
               #       Append Initial state
               # print(root)
               frontier.put(root)
               frontier_Set.add(tuple(map(tuple,root.matrix)))
               #print(frontier)
               #       Set for explored States
               explored=set()
               #explored=[]
               while not frontier.empty(): #     while the queue is not empty 
                    Node=frontier.get()    #     deque state in Queue
                    frontier_Set.remove(tuple(map(tuple,Node.matrix)))
                    
                    print("Expanded:",Node.matrix)
                    explored.add(tuple(map(tuple,Node.matrix))) 
                   # explored.append(Node.mat) 
                    #     Add state to explored set
          
                    if Node.matrix == final : #      if state is the goal state 
                         # End timer
                         end_time = time.time()
                         
                         # Calculate elapsed time
                         elapsed_time = end_time - start_time
                         print("GOAL REACHED !!!\n")
                         # print("Nodes Expanded:")
                         # for i in range(len(explored)):
                         #      print(explored[i])
                         #      print('\n')
                         
                         # Print the path from root to destination;
                         print("Path to goal: " )
                         printPath(Node) 
                         print("cost of path: " ,Node.cost)
                         print("search Depth: ",Node.level)
                         print("Running time: ", elapsed_time,"s") 
                         
                         return  Node     #      Return goal State
                    # Generate all possible children
                    for i in range(4):
                         new_tile_pos = [
                              Node.empty_tile_pos[0] + row[i],
                              Node.empty_tile_pos[1] + col[i], ]
                              
                         if isSafe(new_tile_pos[0], new_tile_pos[1]):
                              
                              # Create a child node
                              child = newNode(Node.matrix,Node.empty_tile_pos,new_tile_pos,Node.level + 1,Node,Node.cost + 1 ,final,)
                              if ((tuple(map(tuple,child.matrix))) not in frontier_Set) and  ((tuple(map(tuple,child.matrix))) not in explored): 
                              #       If the new state is not already in the queue and not already explored enqueue in the queue 
                                   frontier.put(child)
                                   frontier_Set.add(tuple(map(tuple,child.matrix)))
                                   
    
     else :
                    
          
          print("Not Solvable")
          return 
     
def findZero(State):
  for i in range(0,3):
      for j in range (0,3):
          if State[i][j]is None:
              print("Empty at index:",i,j)
              empty_tile_pos=[i,j]
              return empty_tile_pos
          
if __name__ == "__main__":
    
     #Not solvable example
     # initial=([[8,1,2],[None,4,3],[7,6,5]])
     #solvable example
    # 1,2,5,3,4,0,6,7,8
     initial=([[1,2,5],[3,4,None],[6,7,8]])
     final=([[None,1,2],[3,4,5],[6,7,8]])
     
     
     solve_BFS(initial, findZero(initial), final)