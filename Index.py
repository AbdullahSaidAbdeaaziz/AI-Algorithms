import time

path = ["path : "]


def DFS(graph: dict, initial_state: int, goal_state: int):
    path.append(str(initial_state))
    if initial_state == goal_state:  # If founded stop (base case)
        all_path = '->'.join(path[1:])
        print(f"{path[0]}{all_path}")
        time.sleep(2)
    try:
        for leaf in graph[initial_state]:
            DFS(graph, leaf, goal_state)
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
    DFS(graph, initial_state, goal_state)
    print("Founded 🥳!")


if __name__ == "__main__":
    main()
