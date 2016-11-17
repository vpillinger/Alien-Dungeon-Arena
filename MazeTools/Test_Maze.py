import unittest
from MazeTools import Maze as maze

class MazeTest(unittest.TestCase):

    def test_importMaze(self):
        self.assertEquals(False, True)

    def test_generateMaze(self):
        maze = None
        self.assertEquals(maze is not None)


if __name__ == '__main__':
    unittest.main()
