"""This program implements Conway's simple Game of Life in a console window.

classes:
Cell: One Game Of Life cell.
Grid: Playing grid.

functions:
iterate(grid, iterations): Iterate the grid iterations number of times
example(): Default code showing a possible implementation of this module

variables:
None
"""


class Cell:
    """One Game of Life cell.

    attributes:
    x_pos: X position of the cell in the grid: int
    y_pos: Y position of the cell in the grid: int
    value: Current value of the cell, 1 = alive, 0 = dead: int

    methods:
    run_rules(neighbor_count): Runs the Game of Life on a cell and returns its new state
    display(): Prints the correct square character based on the state of the cell
    """

    def __init__(self, x_pos: int, y_pos: int, value: int) -> None:
        """Set various values for new instances of this Cell class

        parameters:
        x_pos: X position of the cell in the grid: int
        y_pos: Y position of the cell in the grid: int
        value: Current value of the cell, 1 = alive, 0 = dead: int

        returns: Nothing: None
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value

    def run_rules(self, neighbor_count: int) -> int:
        """Run the Game of Life's rules on a particular cell

        parameters:
        neighbor_count: Number of alive neighbors this cell has: int

        returns: The cell's new value: int
        """
        new_value = -1
        if neighbor_count not in (2, 3):
            new_value = 0

        if neighbor_count == 3:
            new_value = 1

        if neighbor_count == 2:
            if self.value not in (0, 1):
                raise ValueError
            new_value = self.value

        if new_value == -1:
            raise ValueError
        return new_value

    def display(self) -> str:
        """Display this cell as either a full or empty square

        parameters:
        None

        returns: Correct square character: str
        """
        squares = ["□", "■"]
        return squares[self.value]


class Grid:
    """Playing grid.

    attributes:
    grid: Playing grid itself: list[list[Cell]]
    iteration: Stores the current iteration this grid is on: int
    size: Size of the current square grid; size by size: int

    methods:
    toggle_state(positions): Toggle the state of each cell at each (x, y) postion
    get_neighbors(cell): Return the number of neighbors a particular Cell has
    iterate_grid(): Iterate the grid according to the rules, once
    """

    def __init__(self, size: int) -> None:
        """Set various values for new instances of this Grid class

        parameters:
        size: Size of the current square grid; size by size: int

        returns: Nothing: None
        """
        self.grid = [
            [Cell(x, y, 0) for y in range(1, size + 1)] for x in range(1, size + 1)
        ]
        self.iteration = 0
        self.size = size

    def __str__(self) -> str:
        """Return a string representation of this grid

        parameters:
        None

        returns: String represenation of this grid: str
        """
        return_string = ""
        for row in self.grid:
            for cell in row:
                return_string += f"{cell.display()} "
            return_string += "\n"

        return return_string

    def toggle_state(self, positions: list[tuple[int, int]]) -> None:
        """Toggle the state of each cell at each (x, y) postion

        parameters:
        positions: List of positions to toggle: list[tuple(int, int)]

        returns: Nothing: None
        """
        for row in self.grid:
            for cell in row:
                if (cell.x_pos, cell.y_pos) in positions:
                    if cell.value == 0:
                        cell.value = 1
                    else:
                        cell.value = 0

    def get_neighbors(self, cell: Cell) -> int:
        """Return the number of neighbors a particular Cell has

        parameters:
        cell: Cell to find the number of neighbors of: Cell

        returns: Number of neighbors a cell has: int
        """
        neighbor_count = 0
        temp_x = cell.x_pos
        temp_y = cell.y_pos
        neighbors = [
            (temp_x + 1, temp_y),
            (temp_x - 1, temp_y),
            (temp_x, temp_y + 1),
            (temp_x, temp_y - 1),
            (temp_x + 1, temp_y + 1),
            (temp_x + 1, temp_y - 1),
            (temp_x - 1, temp_y + 1),
            (temp_x - 1, temp_y - 1),
        ]

        for row in self.grid:
            for possible_neighbor in row:
                if (possible_neighbor.x_pos, possible_neighbor.y_pos) in neighbors:
                    neighbor_count += possible_neighbor.value

        return neighbor_count

    def iterate_grid(self) -> None:
        """Iterate the grid according to the rules, once

        parameters:
        None

        returns: Nothing: None
        """
        new_grid = []
        for row in self.grid:
            new_row = []
            for cell in row:
                new_value = cell.run_rules(self.get_neighbors(cell))
                new_row.append(Cell(cell.x_pos, cell.y_pos, new_value))
            new_grid.append(new_row)
        self.grid = new_grid
        self.iteration += 1


def iterate(grid: Grid, iterations: int) -> None:
    """Iterate the grid iterations number of time

    parameters:
    grid: Grid to iterate: Grid
    iterations: Number of times to iterate grid: int

    returns: Nothing: None
    """
    while iterations > 0:
        grid.iterate_grid()
        print(grid)
        iterations -= 1


def example() -> None:
    """Default code showing a possible implementation of this module

    parameters:
    None

    returns: Nothing: None
    """
    play_grid = Grid(6)
    play_grid.toggle_state([(4, 3), (3, 3), (3, 4), (4, 4), (4, 5)])
    print(play_grid)
    iterate(play_grid, 4)


if __name__ == "__main__":
    example()
