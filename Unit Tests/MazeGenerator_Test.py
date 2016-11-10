import unittest, MazeGenerator, numpy as np
from collections import deque


class MyTestCase(unittest.TestCase):

    # Size & Length Tests
    def test_size_0(self):
        """Test whether generate_maze returns an empty numpy array on size 0"""
        maze = MazeGenerator.generate_maze(0)
        self.assertEqual(0, maze.size)
        self.assertEqual((0,), maze.shape)

    def test_size(self):
        """Test whether generate_maze returns a numpy array of the proper size
        and dimensions for several inputs"""
        lengths = [1,5,10]
        for i in lengths:
            maze = MazeGenerator.generate_maze(i)
            self.assertEqual(i*i*4, maze.size)
            self.assertEqual((i,i,4), maze.shape)

    # Graph completeness tests
    def test_completeness(self):
        """Use Breadth-First-Search to test that maze graph is complete (all nodes connected)
        The number of visited nodes should be equal to the maze's size"""
        lengths = [1,5,20,50,1000]
        directions = (-1, 0), (0, 1),(1, 0), (0, -1) #NESW

        for length in lengths:
            maze = MazeGenerator.generate_maze(length)
            q = deque()

            visited = set()
            q.append((0,0))
            while q:
                # pop to visited
                current = q.popleft()
                visited.add(current)

                # get neighbors
                neighbors = []
                for i, adj in enumerate(maze[current[0],current[1]]):
                    if adj:
                        neighbors.append(directions[i])

                # add neighbors to queue
                for neighbor in neighbors:
                    n = (current[0] + neighbor[0], current[1] + neighbor[1])
                    if n not in visited:
                        q.append(n)

            self.assertEqual(maze.size, len(visited) * 4)

# BFS
if __name__ == '__main__':
    unittest.main()
