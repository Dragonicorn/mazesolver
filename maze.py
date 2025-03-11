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
            win,
        ):
        self._win = win
        self._tl = tl
        self._cell_width = cell_size_x
        self._cell_height = cell_size_y
        self._rows = num_rows
        self._cols = num_cols
        self._cells = [[0] * self._cols] * self._rows
        self._create_cells()

    def _create_cells(self):
        for r in range(self._rows):
            for c in range (self._cols):
                tl = Point(self._tl.x + self._cell_width * c, self._tl.y + self._cell_height * r)
                br = Point(tl.x + self._cell_width - 1, tl.y + self._cell_height - 1)
                self._cells[r][c] = Cell(tl, br)
                self._draw_cell(r, c)
                self._animate()

    def _draw_cell(self, r, c):
        self._cells[r][c].draw(self._win.canvas(), "white")

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
