from constants import *
from gui import *
from cell import *

def main():

    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    #line1 = Line(Point(10, 20), Point(48, 64))
    #line2 = Line(Point(100, 200), Point(73, 231))
    #win.draw_line(line1, "white")
    #win.draw_line(line2, "yellow")

    cell1 = Cell(0)
    win.draw_cell(cell1, "white")
    cell2 = Cell(57)
    cell2.has_left_wall = False
    cell2.has_top_wall = False
    win.draw_cell(cell2, "blue")
    cell1.draw_move(win.canvas(), cell2)
    win.wait_for_close()

main()
