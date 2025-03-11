from constants import *
from gui import *
from cell import *

def main():

    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    #line1 = Line(Point(10, 20), Point(48, 64))
    #line2 = Line(Point(100, 200), Point(73, 231))
    #win.draw_line(line1, "white")
    #win.draw_line(line2, "yellow")

    cell = Cell(0)
    win.draw_cell(cell, "white")
    cell = Cell(32)
    cell.has_bottom_wall = False
    win.draw_cell(cell, "yellow")
    cell = Cell(57)
    cell.has_left_wall = False
    cell.has_top_wall = False
    win.draw_cell(cell, "blue")
    cell = Cell(71)
    cell.has_right_wall = False
    cell.has_bottom_wall = False
    win.draw_cell(cell, "green")
    win.wait_for_close()

main()
