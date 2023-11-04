import time


class State:
    def __init__(self, matrix, level=0, parent=None):
        self.matrix = matrix
        self.level = level
        self.parent = parent

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __lt__(self, other):
        return self.matrix < other.matrix

    def __hash__(self):
        return hash(str(self.matrix))

    def is_goal_state(self):
        return self.matrix == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        # return self.matrix ==[1, 2, 5], [3, 4, 0], [6, 7, 8]
        # b l t r

    def get_possible_level(self):
        level = []
        row, col = self.find_blank()
        #top
        if row > 0:
            level.append((-1, 0))
        #bottom
        if row < 2:
            level.append((1, 0))
        #left
        if col > 0:
            level.append((0, -1))
        #right
        if col < 2:
            level.append((0, 1))
        return level

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == 0:
                    return i, j

    def apply_move(self, move):
        matrix = [row[:] for row in self.matrix]
        row, col = self.find_blank()
        drow, dcol = move
        matrix[row][col], matrix[row + drow][col + dcol] = matrix[row + drow][col + dcol], matrix[row][col]
        return State(matrix, self.level + 1, self)

    def print_path(self, hashmap, initial_state, search_depth, explored):
        if hashmap is None:
            print("No solution found.")
            return
        node = self
        # x = self.matrix
        """Prints the path from the root node to the given node"""
        path = []
        path.append(node.matrix)
        while hashmap[node] != initial_state:
            path.append(hashmap[node].matrix)
            node = hashmap[node]
        path.append(initial_state.matrix)
        path.reverse()
        for i, step in enumerate(path):
            print(f'Step {i + 1}: {step}')
        print(f'Goal state reached!')
        print(f"cost of the path is {len(path) - 1} ")
        print(f"search depth is :{search_depth}")
        print(f"Num of explored nodes is :{len(explored)}")


        # for ex in explored:
        #     print(ex.matrix)


def dfs_search(initial_state):
    start = time.time()
    stack = [initial_state]
    search_depth = 0
    explored = set()
    stacksearch = set()
    stacksearch.add(initial_state)
    hashmap_depth = {}
    hashmap = {}
    hashmap[initial_state] = initial_state
    while stack:
        current_state = stack.pop()
        search_depth = max(search_depth, current_state.level)
        stacksearch.remove(current_state)
        # hashmap[current_state] = current_state.parent
        if current_state.is_goal_state():
            end = time.time()
            current_state.print_path(hashmap, initial_state, search_depth, explored)
            print("The time of execution of DFS :",(end - start) * 10 ** 3, "ms")
            print(f"Num of explored nodes is :{len(explored)}")
            return current_state
            # return current_state.get_solution() ,search_depth

        explored.add(current_state)

        possible_level = current_state.get_possible_level()

        for move in possible_level:
            new_state = current_state.apply_move(move)
            if new_state not in explored and new_state not in stacksearch:
                stack.append(new_state)
                hashmap[new_state] = current_state
                stacksearch.add(new_state)

    return None


if __name__ == "__main__":
    
    initial_puzzle = ([[1,2,5],[3,4,0],[6,7,8]])
    # initial_puzzle =[[1, 0, 2], [3, 4, 5], [6, 7, 8]]

    initial_state = State(initial_puzzle)
   

    solution = dfs_search(initial_state)