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
    index_blank = current_puzzle.index(-1)
    guess_directions = [index_blank + 1,  # left
                        index_blank - 1,  # right
                        index_blank - (len(current_puzzle) // 2 - 1),  # down
                        index_blank + (len(current_puzzle) // 2 - 1)  # up
                        ]
    # check left & right direction
    flag = True
    if index_blank % 3 == 2:
        guess_directions.remove(guess_directions[0])
        flag = False
    if index_blank % 3 == 0:
        if not flag:
            guess_directions.remove(guess_directions[0])
        else:
            guess_directions.remove(guess_directions[1])

    # check up, down direction, and if left & right is valid
    right_directions = list(filter(lambda x: 0 <= x < len(current_puzzle), guess_directions))

    return right_directions


def print_grid(grid: list[int]) -> None:
    for i, v in enumerate(grid):
        if i % 3 == 0:
            print()
        print(v, "", sep=" ", end="")
    print("\n#" * 40)


def dfs(grid: list[int]):
    heuristic_value = calculate_heuristic_misplaced_tails(grid)
    if heuristic_value == 0:
        return
    possible_moves = check_direction(grid)
    for i in possible_moves:
        temp = grid.copy()
        blank_temp = temp.index(-1)
        generate_new_swap_list(i, blank_temp, temp)
        print(temp)
        dfs(temp)
        if calculate_heuristic_misplaced_tails(temp) == 0:
            break


def main():
    # initial state of problem of 8-puzzle
    initial_state = [
        1, 2, 3,  # 0 1 2
        4, 5, 6,  # 3 4 5
        8, -1, 7  # 6 7 8
    ]
    dfs(initial_state) # not finish yet


if __name__ == "__main__":
    main()
