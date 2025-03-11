from gui import *

def main():
    win = Window(800,600)
    line1 = Line(Point(10, 20), Point(48, 64))
    line2 = Line(Point(100, 200), Point(73, 231))
    win.draw_line(line1, "white")
    win.draw_line(line2, "yellow")
    win.wait_for_close()

main()
