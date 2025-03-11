from constants import *
from gui import *
from cell import *
from maze import *

def main():

    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    #line1 = Line(Point(10, 20), Point(48, 64))
    #line2 = Line(Point(100, 200), Point(73, 231))
    #win.draw_line(line1, "white")
    #win.draw_line(line2, "yellow")

    maze_width = 12
    maze_height = 10
    tl = Point((WINDOW_WIDTH - CELL_SIZE * maze_width) // 2, (WINDOW_HEIGHT - CELL_SIZE * maze_height) // 2)
    print("Top Left = ", tl.x, tl.y)
    maze = Maze(tl, maze_height, maze_width, CELL_SIZE, CELL_SIZE, win)

    win.wait_for_close()

main()
