from MazeTools import MazeGenerator


class Maze:

    def __init__(self, maze):

        self.maze = maze

    def is_adjacent(self, first, second):
        """
        Return true if the two locations are adjacent to each other.
        Else return false.

        :param first: a tuple (i,j) for the first location
        :param second: a tuple (i,j) for the second location
        """
        return False

    def go_direction(self, start, direction):
        """
        Return a list of tuples that represents the straight-line path of
        going right in the specified direction until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """

    def go_east(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right east until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """

    def go_west(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right west until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """

    def go_north(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right north until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """

    def go_south(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right east until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """

    def bfs(self, stop_function):
        """
        Perform a breadth first search for the specified stop_function.
        Once the stop_function returns true, then return the path to the location specified
        by the stop function.

        :param stop_function: a function that takes a tuple (i,j)
            and returns true if the current location is the destination location
        :return: a list of tuples that is the path to the space on which stop_function
            returned true
        """

    def print_maze(self):

        line = ""
        for row in self.maze:  # top of maze
            line += " _"
        print(line)

        # We only need to do one side of each connection: so start in top-left look east&south.
        for i, row in enumerate(self.maze):
            line = "|"  # left of maze
            for j, cell in enumerate(row):
                if (i + 1, j) in cell:
                    line += " "
                else:
                    line += "_"
                if (i, j + 1) in cell:
                    line += " "
                else:
                    line += "|"
            print(line)

def make_maze(length):  # is this kind of method pythonic?
    """
    Factory method for making mazes that are already pre-generated at the specified size

    :param length: the dimensions of the maze (length X length)
    :return: Maze Object
    """
    return Maze(MazeGenerator.generate_maze(length))