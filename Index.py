import time

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


'''
           [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
           ]
 -1 --> blink tail
'''


def calculate_heuristic_misplaced_tails(puzzle: list[list]) -> int:
    """
    calculate of heuristic of misplaced tails to compare for it.
    """
    heuristic_value: int = 0
    for i, inner in enumerate(puzzle):
        if inner == -1:
            continue
        if i + 1 != inner:
            heuristic_value += 1

    return heuristic_value


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
    dl = [1, 5, 4,
          3, 2, 6,
          7, 8, -1]
    print(calculate_heuristic_misplaced_tails(dl))


if __name__ == "__main__":
    main()
