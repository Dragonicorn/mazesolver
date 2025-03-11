from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.canvas = Canvas(cnf={"bg":"black"})
        self.__root.canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.active = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.active = True
        while self.active == True:
            self.redraw()
        
    def close(self):
        self.active = False

def main():
    win = Window(800,600)
    win.wait_for_close()

main()
