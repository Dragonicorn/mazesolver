import unittest
from gui import *
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_small(self):
        num_rows = 1
        num_cols = 1
        m1 = Maze(Point(0,0), num_rows, num_cols, 1, 1)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_std(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(Point(0,0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        num_rows = 40
        num_cols = 30
        m1 = Maze(Point(0,0), num_rows, num_cols, 20, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_oversize(self):
        num_rows = 64
        num_cols = 64
        m1 = Maze(Point(0,0), num_rows, num_cols, 100, 100)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()