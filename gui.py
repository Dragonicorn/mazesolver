from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.canvas = Canvas(cnf={"bg":"black"})
        self.__root.canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.active = False

    def draw_line(self, line, fill_color):
        line.draw(self.__root.canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.active = True
        while self.active == True:
            self.redraw()
        
    def close(self):
        self.active = False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2)
