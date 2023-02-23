"""This program implements the Game of Life in an easier to use format than gameoflife.py.

classes:
None

functions:
iterate(grid, iterations): Iterate the grid iterations number of times
run(grid): Iterate the grid a max number of times or until two consecutive states are the same
main(): Main program loop

variables:
None
"""
import gameoflife as gol


def iterate(grid: gol.Grid, iterations: int = 1) -> None:
    """Iterate play_grid iterations times

    parameters:
    grid: Grid to be iterated: gol.Grid
    iterations: Number of times to iterate: int

    returns: Nothing: None
    """
    while iterations != 0:
        grid.iterate_grid()
        print(grid)
        iterations -= 1


def run(grid: gol.Grid):
    """Iterate the grid a max number of times or until two consecutive states are the same

    parameters:
    grid: Grid object to iterate: gol.Grid

    returns: Nothing: None
    """
    iterations = 0
    max_iterations = 20
    previous_state: list[int] = []
    current_state: list[int] = []

    for row in grid.grid:
        for cell in row:
            current_state.append(cell.value)

    while (current_state != previous_state) and iterations < max_iterations:
        previous_state = current_state[:]

        iterate(grid)
        current_state.clear()
        for row in grid.grid:
            for cell in row:
                current_state.append(cell.value)

        iterations += 1


def main() -> None:
    """Create grid then allow the user to look at its behavior over time

    parameters:
    None

    returns: Nothing: None
    """
    play_grid = gol.Grid(int(input("How large would you like the grid to be? ")))
    print(play_grid)

    print("Toggle a cell by providing x, y coordinates from the top left.")
    print('Enter "quit" to exit this setup phase.')
    print('Enter "help" to see this help again.')

    # generate grid
    while True:
        command = input("> ")
        if command == "quit":
            break

        if command == "help":
            print(
                'Toggle a cell by providing "x, y" coordinates from the top left,'
                "starting with (1, 1)."
            )
            print('Enter "quit" to exit this setup phase.')
            print('Enter "help" to see this help again.')
            continue

        try:
            pos = [int(command.split(", ")[0]), int(command.split(", ")[1])]

            if pos[0] > play_grid.size or pos[1] > play_grid.size:
                print('Invalid coordinate. Enter "help" for help.')
                continue

            play_grid.toggle_state([(pos[1], pos[0])])
            print(play_grid)

        except ValueError:
            print('Invalid coordinate. Enter "help" for help.')
            continue

        except IndexError:
            print(
                "Ensure your inputted coordinate consists \
                    of two numbers separated by a comma and a space."
            )

    # run iterations on created grid
    while True:
        command = input(
            "Press enter for next iteration,"
            ' "run" to keep iterating until two consecutive iterations appear\n'
            '"go [number]" to run that many iterations, or "quit" to exit. '
        )

        if command.startswith("go"):
            print(play_grid)
            iterate(play_grid, int(command.split(" ")[1]))

        elif command == "run":
            print(play_grid)
            run(play_grid)
            break

        elif command == "quit":
            break

        else:
            iterate(play_grid)


if __name__ == "__main__":
    main()
