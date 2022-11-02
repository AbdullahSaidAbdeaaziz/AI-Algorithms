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
            for leaf in graph[initial_state]:
                DFS(graph, leaf, goal_state, visited)  # check another leaf node.
        except KeyError:
            pass


def main():
    """
                     1
                 /   |   \
               3     4    5
            / | \  /  \
          7  8 9   6  5
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
    DFS(graph, initial_state, goal_state, visited)
    print("YAYA 🥳!")


if __name__ == "__main__":
    main()
