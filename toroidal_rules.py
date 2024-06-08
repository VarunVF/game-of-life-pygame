def update_state(old_state: list[list[int]]):
    # assuming a uniform rectangular grid old_state.
    # where all rows have the same length
    # and all columns have the same length
    grid_width = len(old_state[0])
    grid_height = len(old_state)

    new_state = [[cell for cell in row] for row in old_state]

    for row in range(grid_height):
        for col in range(grid_width):
            neighbours = (
                    old_state[row][(col + 1) % grid_width]  # right
                    + old_state[row][(col - 1) % grid_width]  # left
                    + old_state[(row - 1) % grid_height][col]  # upper
                    + old_state[(row + 1) % grid_height][col]  # lower
                    + old_state[(row - 1) % grid_height][(col - 1) % grid_width]  # upper left
                    + old_state[(row + 1) % grid_height][(col + 1) % grid_width]  # lower right
                    + old_state[(row - 1) % grid_height][(col + 1) % grid_width]  # upper right
                    + old_state[(row + 1) % grid_height][(col - 1) % grid_width]  # lower left
            )

            # if current cell is live
            if new_state[row][col] == 1:
                # live cell with < 2 neighbours dies
                if neighbours < 2:
                    new_state[row][col] = 0
                # live cell with 2 or 3 neighbours live
                elif neighbours in (2, 3):
                    pass
                # live cell with more than 3 neighbours dies
                else:
                    new_state[row][col] = 0
                continue

            # if current cell is dead
            else:
                # dead cell with 3 neighbours becomes live
                if neighbours == 3:
                    new_state[row][col] = 1
                continue

    return new_state
