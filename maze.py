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
        ):
        self._win = win
        self._tl = tl
        self._cell_width = cell_size_x
        self._cell_height = cell_size_y
        self._rows = num_rows
        self._cols = num_cols
        self._cells = [[0 for c in range(self._cols)] for r in range(self._rows)]
        self._create_cells()

    def _create_cells(self):
        for r in range(self._rows):
            for c in range (self._cols):
                tl = Point(self._tl.x + self._cell_width * c, self._tl.y + self._cell_height * r)
                br = Point(tl.x + self._cell_width - 1, tl.y + self._cell_height - 1)
                self._cells[r][c] = Cell(tl, br)
                if self._win != None:
                    self._draw_cell(r, c)
                    self._animate()
        self._break_entrance_and_exit()

    def _draw_cell(self, r, c):
        self._cells[r][c].draw(self._win.canvas(), "white")

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._rows - 1][self._cols - 1].has_bottom_wall = False
        if self._win != None:
            self._draw_cell(0, 0)
            self._draw_cell(self._rows - 1, self._cols - 1)