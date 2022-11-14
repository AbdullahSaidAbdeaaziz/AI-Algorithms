
path = ["path : "]


def DFS(graph: dict, initial_state: int, goal_state: int, visited: set):
    if initial_state not in visited:
        path.append(str(initial_state))
        visited.add(initial_state)
        if initial_state == goal_state:  # Find goal state.
            all_path = '->'.join(path[1:])
            print(f"{path[0]}{all_path}")
            return
        try:
            DFS(graph, initial_state, goal_state, visited)
            for leaf in graph[initial_state]:
                DFS(graph, leaf, goal_state, visited)  # check another leaf node.
        except KeyError:
            pass


# TODO Islam Task
def BFS(graph: dict, initial_state: int, goal_state: int, visited: set):
    # down here boy
    pass


def calculate_heuristic_misplaced_tails(puzzle: list[int]) -> int:
    """
    calculate of heuristic of misplaced tails to compare for it.
    '''
               [
                1, 2, 3,
                4, 5, 6,
                7, 8, -1
               ]
        -1 --> blink tail
    '''
    """
    heuristic_value: int = 0
    for i, inner in enumerate(puzzle):
        if inner == -1:
            continue
        if i + 1 != inner:
            heuristic_value += 1

    return heuristic_value


def generate_new_swap_list(index, i, matrix) -> list:

    matrix[index], matrix[i] = matrix[i], matrix[index]
    return matrix


def check_direction(current_puzzle: list[int]) -> int:
    index_blank = current_puzzle.index(-1)  # get value of index
    temp = current_puzzle.copy()
    minim = id(int)
    # right, left, up, down
    guess_direction = [index_blank + 1, index_blank - 1, index_blank + (len(current_puzzle)//2 - 1), index_blank - (len(current_puzzle)//2 - 1)]
    available_direction = list(filter(lambda x: 0 <= x < len(current_puzzle), guess_direction))
    print(available_direction)
    for i in available_direction:
        minim = min(calculate_heuristic_misplaced_tails(generate_new_swap_list(index_blank, i, temp)), minim)
        temp = current_puzzle
    return minim


def main():
    """
                     1
                   / | \
                 /   |  \
               3     4   5
            / | \  /  \
          7  8  9 6   5
    """
    graph = {
        1: [3, 4, 5],
        3: [7, 8, 4],
        4: [6, 5],
        5: []
    }
    initial_state = 1
    goal_state = 4
    visited = set()
    # DFS(graph, initial_state, goal_state, visited)
    # print("YAY 🥳!")
    """
          0  1  2
          3  4  5 
          6  7  8 
    """
    dl = [8, 5, 4,
          3, 1, 6,
          7, -1, 2]
    print(calculate_heuristic_misplaced_tails(dl))
    print(check_direction(dl))


if __name__ == "__main__":
    main()
