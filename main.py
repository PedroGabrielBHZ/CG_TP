from tkinter import Tk
from windows import MainWindow


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Computer Graphics Showcase")
        MainWindow(self)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
