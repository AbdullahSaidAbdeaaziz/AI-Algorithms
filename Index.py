import time


def calculate_heuristic_misplaced_tails(puzzle: list[int]) -> int:
    """

    Args:
        puzzle: current state.

    Returns:
        calculate no.of mis-placed value not in right place in puzzle.
    """
    heuristic_value: int = 0
    for i, inner in enumerate(puzzle):
        if inner == -1:
            continue
        if i + 1 != inner:
            heuristic_value += 1

    return heuristic_value


def generate_new_swap_list(index: int, i: int, matrix: list[int]) -> None:
    """

    Args:
        index: index in list.
        i: another index in list.
        matrix: current list.

    Returns:
        swap indices(index, i) it's value in matrix to generate new list.
    """
    matrix[index], matrix[i] = matrix[i], matrix[index]


def check_direction(current_puzzle: list[int]) -> list:
    """

    Args:
        current_puzzle: current state in 8-puzzle.

    Returns:
        all possible directions for blank tail to move it in current_puzzle.
    """
    index_blank: int = current_puzzle.index(-1)
    guess_directions: list = [index_blank + 1,  # left
                              index_blank - 1,  # right
                              index_blank - (len(current_puzzle) // 2 - 1),  # down
                              index_blank + (len(current_puzzle) // 2 - 1)  # up
                              ]
    # check left & right direction
    flag: bool = True
    if index_blank % 3 == 2:
        guess_directions.remove(guess_directions[0])
        flag: bool = False
    if index_blank % 3 == 0:
        if not flag:
            guess_directions.remove(guess_directions[0])
        else:
            guess_directions.remove(guess_directions[1])

    # check up, down direction, and if left & right is valid
    right_directions: list = list(filter(lambda x: 0 <= x < len(current_puzzle), guess_directions))

    return right_directions


def get_inversion_count(grid: list[int]) -> int:
    inv_count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if grid[j] != -1 and grid[i] != -1 and grid[i] > grid[j]:
                inv_count += 1
    return inv_count


def is_solvable(grid: list[int]) -> bool:
    inversion_count = get_inversion_count(grid)
    return inversion_count % 2 == 0


def print_grid(grid: list[list[int]]) -> None:
    if not grid:
        return
    for i, v in enumerate(grid):
        for x, j in enumerate(v):
            if x % 3 == 0:
                print()
            print(f"{j} ", end="")
        print(f"\n{'#' * 40}({i + 1})")


def dfs(grid: list[int]) -> None:
    """

    Args:
        grid: initial state of 8-puzzle problem

    Returns:
        Depth path to reach to goal state of 8-puzzle problem
    """
    if not is_solvable(grid):
        print("this is state is not solvable in 8-puzzle")
        return None
    stack, path = [grid], []
    while stack:
        expand_node = stack.pop()
        if calculate_heuristic_misplaced_tails(expand_node) == 0:
            path.append(expand_node)
            break
        if expand_node in path:
            continue
        path.append(expand_node)
        index_blank = expand_node.index(-1)
        directions_blank = check_direction(expand_node)
        for move in directions_blank:
            expand_node_temp = expand_node.copy()
            generate_new_swap_list(index_blank, move, expand_node_temp)
            if is_solvable(expand_node_temp):
                stack.append(expand_node_temp)

    return path


def main():
    # initial state of problem of 8-puzzle
    initial_state = [
        1, 2, 3,
        4, -1, 5,
        8, 6, 7
    ]
    # print(is_solvable(initial_state))
    """
    goal state
    1 2 3 
    4 5 6
    7 8 -1 
    """
    print(f"{'😍' * 40} Start DFS {'😍' * 40}")
    print_grid(dfs(initial_state))
    print(f"{'😍' * 40} End DFS {'😍' * 40}")


if __name__ == "__main__":
    main()
