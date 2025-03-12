import random
import time
from constants import *
from cell import *
from gui import *

class Maze():
    def __init__(
            self,
            tl,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win = None,
            seed = None,
        ):
        if seed != None:
            random.seed(seed)
        self._win = win
        self._tl = tl
        self._cell_width = cell_size_x
        self._cell_height = cell_size_y
        self._rows = num_rows
        self._cols = num_cols
        self._cells = [[0 for c in range(self._cols)] for r in range(self._rows)]
        self._create_cells()
        self._break_entrance_and_exit()
        self._queue = []
        self._break_walls_r(0, 0)
        self._queue = []
        self._reset_cells_visited()

    def _create_cells(self):
        for r in range(self._rows):
            for c in range (self._cols):
                tl = Point(self._tl.x + self._cell_width * c, self._tl.y + self._cell_height * r)
                br = Point(tl.x + self._cell_width - 1, tl.y + self._cell_height - 1)
                self._cells[r][c] = Cell(tl, br)
                if self._win != None:
                    self._draw_cell(r, c)
                    #self._animate(0.02)

    def _draw_cell(self, r, c):
        self._cells[r][c].draw(self._win.canvas(), "white")

    def _animate(self, duration):
        self._win.redraw()
        time.sleep(duration)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._rows - 1][self._cols - 1].has_bottom_wall = False
        if self._win != None:
            self._draw_cell(0, 0)
            self._draw_cell(self._rows - 1, self._cols - 1)
    
    def _break_walls_r(self, i, j):
        # Push current cell onto stack
        self._queue.append((i, j))
        # Mark current cell as visited
        self._cells[j][i].visited = True
        # Randomly select unvisited adjacent cell
        while True:
            neighbors = []
            if 0 < i:
                if not self._cells[j][i - 1].visited:
                    neighbors.append((i - 1, j))
            if i < self._cols - 1:
                if not self._cells[j][i + 1].visited:
                    neighbors.append((i + 1, j))
            if 0 < j:
                if not self._cells[j - 1][i].visited:
                    neighbors.append((i, j - 1))
            if j < self._rows - 1:
                if not self._cells[j + 1][i].visited:
                    neighbors.append((i, j + 1))
            if len(neighbors) != 0:
                neighbor = random.randint(0, len(neighbors) - 1)
                (next_i, next_j) = neighbors[neighbor]
                if next_i < i:
                    self._cells[j][i].has_left_wall = False
                    self._cells[j][next_i].has_right_wall = False
                elif next_i > i:
                    self._cells[j][i].has_right_wall = False
                    self._cells[j][next_i].has_left_wall = False
                elif next_j < j:
                    self._cells[j][i].has_top_wall = False
                    self._cells[next_j][i].has_bottom_wall = False
                elif next_j > j:
                    self._cells[j][i].has_bottom_wall = False
                    self._cells[next_j][i].has_top_wall = False
                if self._win != None:
                    self._draw_cell(j, i)
                    self._draw_cell(next_j, next_i)
                    self._animate(0.01)
                self._break_walls_r(next_i, next_j)
            else:
                if len(self._queue) > 0:
                    (i, j) = self._queue.pop()
                else:
                    break

    def _reset_cells_visited(self):
        for r in range(self._rows):
            for c in range(self._cols):
                self._cells[r][c].visited = False
    
    def _solve_r(self, i, j):
        # Push current cell onto stack
        self._queue.append((i, j))
        # Mark current cell as visited
        self._cells[j][i].visited = True

        # Check for maze exit cell
        if (i == self._cols - 1) and (j == self._rows - 1):
            return True
        # Check for next cell to visit
        next_i = i
        next_j = j
        undo = False
        # Check for unvisited cell to the left
        if 0 < i:
            if not self._cells[j][i].has_left_wall:
                if not self._cells[j][i - 1].visited:
                    next_i = i - 1
        # Check for unvisited cell to the right
        if (next_i == i) and (i < self._cols - 1):
            if not self._cells[j][i].has_right_wall:
                if not self._cells[j][i + 1].visited:
                    next_i = i + 1
        # Check for unvisited cell above
        if (next_i == i) and (0 < j):
            if not self._cells[j][i].has_top_wall:
                if not self._cells[j - 1][i].visited:
                    next_j = j - 1
        # Check for unvisited cell below
        if (next_i == i) and (next_j == j) and (j < self._rows - 1):
            if not self._cells[j][i].has_bottom_wall:
                if not self._cells[j + 1][i].visited:
                    next_j = j + 1
        duration = 0.05
        if (next_i == i) and (next_j == j):
            undo = True
            duration = 0.5
            if len(self._queue) > 0:
                # Discard current node
                (next_i, next_j) = self._queue.pop()
                # Backtrack to previous node
                (next_i, next_j) = self._queue.pop()
            else:
                return False
        if self._win != None:
            self._cells[j][i].draw_move(self._win.canvas(), self._cells[next_j][next_i], undo)
        if self._win != None:
            self._animate(duration)
        return self._solve_r(next_i, next_j)

    def solve(self):
        return self._solve_r(0, 0)
