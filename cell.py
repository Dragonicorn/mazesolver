from constants import *
from gui import *

class Cell():
    def __init__(self, tl, br):
        self._x1 = tl.x
        self._y1 = tl.y
        self._x2 = br.x
        self._y2 = br.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def center(self):
        return Point(self._x1 + (self._x2 - self._x1) // 2, self._y1 + (self._y2 - self._y1) // 2)

    def draw(self, canvas, fill_color):
        if self.has_left_wall:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(canvas, fill_color)
        if self.has_right_wall:
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(canvas, fill_color)
        if self.has_top_wall:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(canvas, fill_color)
        if self.has_bottom_wall:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(canvas, fill_color)

    def draw_move(self, canvas, to_cell, undo=False):
        Line(self.center(), to_cell.center()).draw(canvas, "gray" if undo else "red")