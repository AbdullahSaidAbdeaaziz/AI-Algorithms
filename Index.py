from __future__ import annotations

import queue
import time
from typing import Optional, Any, Tuple, List


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


def check_direction(current_puzzle: list[int]) -> tuple[list, list]:
    """

    Args:
        current_puzzle: current state in 8-puzzle.

    Returns:
        all possible directions (values , directions) for blank tail to move it in current_puzzle .
    """
    index_blank: int = current_puzzle.index(-1)
    guess_directions: dict = {index_blank - 1: "left",  # left
                              index_blank - (len(current_puzzle) // 2 - 1): "up",  # up
                              index_blank + (len(current_puzzle) // 2 - 1): "down",  # down
                              index_blank + 1: "right",  # right
                              }
    # check left & right direction
    if index_blank % 3 == 2:
        guess_directions.pop(index_blank + 1)
    if index_blank % 3 == 0:
        guess_directions.pop(index_blank - 1)

    # check up, down direction, and if left & right is valid
    right_directions: list = list(filter(lambda x: 0 <= x < len(current_puzzle), guess_directions))
    right_moves: list = [v for k, v in guess_directions.items() if 0 <= k < len(current_puzzle)]
    # right_directions = guess_directions.copy()
    # for key, value in guess_directions.items():
    #   if (key < 0 or key >= len(current_puzzle)):
    #        right_directions.pop(key)
    return right_directions, right_moves


def get_inversion_count(grid: list[int]) -> int:
    """
        Args:
            grid: state of 8-puzzle problem

        Returns:
            int number of inversion count for 8-puzzle problem
    """
    inv_count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if grid[j] != -1 and grid[i] != -1 and grid[i] > grid[j]:
                inv_count += 1
    return inv_count


def is_solvable(grid: list[int]) -> bool:
    """

    Args:
        grid: state of 8-puzzle problem

    Returns:
        check if grid can be solved or not

    """
    inversion_count = get_inversion_count(grid)
    return inversion_count % 2 == 0


def print_grid(grid: list[list[int]], directions: list[str]) -> None:
    """

    Args:
        directions:
        grid: state of 8-puzzle problem

    Returns:
        None (print grid with its move that performed)

    """
    if not grid:
        return
    for v, direct in zip(enumerate(grid), directions):
        if v[0] != 0:
            print(f"\t{direct}")
        for x, j in enumerate(v[1]):
            if x % 3 == 0:
                print()
            print(f"{j} ", end="")
        print(f"\n{'#' * 40}({v[0] + 1})")


def dfs(grid: list[int]) -> None | tuple[list[int], list[int]]:
    """

    Args:
        grid: initial state of 8-puzzle problem

    Returns:
        Depth path to reach to goal state of 8-puzzle problem
    """
    if not is_solvable(grid):
        print("this is state is not solvable in 8-puzzle")
        return None
    stack, path, directions = [grid], [], []
    original_directions: list = []
    while stack:
        direct: str = ""
        expand_node = stack.pop()
        if directions:
            direct = directions.pop()
        if calculate_heuristic_misplaced_tails(expand_node) == 0:
            original_directions.append(direct)
            path.append(expand_node)
            break
        if expand_node in path:
            continue
        path.append(expand_node)
        if direct:
            original_directions.append(direct)
        index_blank = expand_node.index(-1)
        directions_blank, blank_moves = check_direction(expand_node)
        for move, direction in zip(directions_blank, blank_moves):
            expand_node_temp = expand_node.copy()
            generate_new_swap_list(index_blank, move, expand_node_temp)
            if is_solvable(expand_node_temp):
                directions.append(direction)
                stack.append(expand_node_temp)
    if len(path) > len(original_directions):
        temp = original_directions.copy()
        original_directions.clear()
        original_directions.append(None)
        original_directions += temp

    return path, original_directions


def bfs(grid: list[int]) -> tuple[list[Any], list] | None:
    """
        Args:
            grid: initial state of 8-puzzle problem

        Returns:
            reach to goal state of 8-puzzle problem by BFS Algorithm
    """
    if not is_solvable(grid):
        print("this is state is not solvable in 8-puzzle")
        return None

    q = queue.Queue()
    directions = queue.Queue()
    q.put(grid)
    path = []
    original_directions: list = []

    while q:
        direct: str = ""
        expand_node = q.get()
        if not directions.empty():
            direct = directions.get()
        if calculate_heuristic_misplaced_tails(expand_node) == 0:
            original_directions.append(direct)
            path.append(expand_node)
            break
        if expand_node in path:
            continue
        path.append(expand_node)
        if direct:
            original_directions.append(direct)
        index_blank = expand_node.index(-1)
        directions_blank, blank_moves = check_direction(expand_node)
        for move, direction in zip(directions_blank, blank_moves):
            expand_node_temp = expand_node.copy()
            generate_new_swap_list(index_blank, move, expand_node_temp)
            if is_solvable(expand_node_temp):
                directions.put(direction)
                q.put(expand_node_temp)

    if len(path) > len(original_directions):
        temp = original_directions.copy()
        original_directions.clear()
        original_directions.append(None)
        original_directions += temp

    return path, original_directions


def main():
    # initial state of problem of 8-puzzle
    initial_state = [
        1, 2, 3,
        4, 5, 6,
        -1, 7, 8
    ]

    # -------------------------------------------
    # DFS Algorithm time: 52.25959587097168
    # BFS Algorithm time: 1.3240139484405518
    # initial_state = [
    #     1, 2, 3,
    #     4, 5, -1,
    #     6, 7, 8
    # ]

    """
    goal state
    1 2 3 
    4 5 6
    7 8 -1 
    """
    # DFS Algorithm
    # --------------
    start = time.time()
    print(f"{'😍' * 20} Start DFS {'😍' * 20}")
    values, directions = dfs(initial_state)
    # print(directions, len(directions))
    # print(values, len(values))
    # v, d = check_direction(initial_state)
    # print(v, len(v))
    # print(d, len(d))
    print_grid(values, directions)
    print(f"{'😍' * 20} End DFS {'😍' * 20}")
    end = time.time()
    print(f"DFS Algorithm time: {end - start}")

    # BFS Algorithm
    # --------------
    start = time.time()
    print(f"{'😍' * 20} Start BFS {'😍' * 20}")
    values, directions = bfs(initial_state)
    print_grid(values, directions)
    print(f"{'😍' * 20} End BFS {'😍' * 20}")
    end = time.time()
    print(f"BFS Algorithm time: {end - start}")


if __name__ == "__main__":
    main()
