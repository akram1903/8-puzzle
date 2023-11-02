import time


class State:
    def __init__(self, twoDarray, moves=0, parent=None):
        self.twoDarray = twoDarray
        self.moves = moves
        self.parent = parent

    def __eq__(self, other):
        return self.twoDarray == other.twoDarray

    def __lt__(self, other):
        return self.twoDarray < other.twoDarray

    def __hash__(self):
        return hash(str(self.twoDarray))

    def is_goal_state(self):
        return self.twoDarray == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        # return self.twoDarray ==[1, 2, 5], [3, 4, 0], [6, 7, 8]
        # b l t r

    def get_possible_moves(self):
        moves = []
        row, col = self.find_blank()
        if row > 0:
            moves.append((-1, 0))
        if row < 2:
            moves.append((1, 0))
        if col > 0:
            moves.append((0, -1))
        if col < 2:
            moves.append((0, 1))
        return moves

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.twoDarray[i][j] == 0:
                    return i, j

    def apply_move(self, move):
        twoDarray = [row[:] for row in self.twoDarray]
        row, col = self.find_blank()
        drow, dcol = move
        twoDarray[row][col], twoDarray[row + drow][col + dcol] = twoDarray[row + drow][col + dcol], twoDarray[row][col]
        return State(twoDarray, self.moves + 1, self)

    def print_path(self, hashmap, initial_state, search_depth, explored):
        if hashmap is None:
            print("No solution found.")
            return
        node = self
        # x = self.twoDarray
        """Prints the path from the root node to the given node"""
        path = []
        path.append(node.twoDarray)
        while hashmap[node] != initial_state:
            path.append(hashmap[node].twoDarray)
            node = hashmap[node]
        path.append(initial_state.twoDarray)
        path.reverse()
        for i, step in enumerate(path):
            print(f'Step {i + 1}: {step}')
        print(f'Goal state reached!')
        print(f"cost of the path is {len(path) - 1} ")
        print(f"search depth is :{search_depth}")

        # for ex in explored:
        #     print(ex)


def dfs_search(initial_state):
    stack = [initial_state]
    search_depth = 0
    explored = set()
    stacksearch = set()
    # stacksearch.add(initial_state)
    stacksearch.add(tuple(map(tuple, initial_state.twoDarray)))
    hashmap_depth = {}
    hashmap = {}
    hashmap[initial_state] = initial_state
    while stack:
        current_state = stack.pop()
        search_depth = max(search_depth,current_state.moves)
        stacksearch.remove(tuple(map(tuple,current_state.twoDarray)))
        # hashmap[current_state] = current_state.parent
        if current_state.is_goal_state():
            current_state.print_path(hashmap, initial_state, search_depth, explored)
            return current_state
            # return current_state.get_solution() ,search_depth

        explored.add(tuple(map(tuple,current_state.twoDarray)))

        possible_moves = current_state.get_possible_moves()

        for move in possible_moves:
            new_state = current_state.apply_move(move)
            if new_state not in explored and new_state not in stacksearch:
                stack.append(new_state)
                hashmap[new_state] = current_state
                stacksearch.add(tuple(map(tuple,current_state.twoDarray)))

    return None


if __name__ == "__main__":
    initial_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # initial_puzzle =[[1, 0, 2], [3, 4, 5], [6, 7, 8]]

    initial_state = State(initial_puzzle)
    start = time.time()

    solution = dfs_search(initial_state)
    end = time.time()
    print("The time of execution of DFS :",
          (end - start) * 10 ** 3, "ms")

