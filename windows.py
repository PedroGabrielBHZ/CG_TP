# windows.py
from tkinter import Frame, Button, Canvas, Entry, StringVar, Label
from algorithms import bresenham, dda

pixel_size = 2


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, width=800, height=600)
        self.canvas.grid()

        self.x0_var = StringVar()
        self.y0_var = StringVar()
        self.x1_var = StringVar()
        self.y1_var = StringVar()

        self.x0_label = Label(self, text="x0:")
        self.y0_label = Label(self, text="y0:")
        self.x1_label = Label(self, text="x1:")
        self.y1_label = Label(self, text="y1:")

        self.x0_entry = Entry(self, textvariable=self.x0_var)
        self.y0_entry = Entry(self, textvariable=self.y0_var)
        self.x1_entry = Entry(self, textvariable=self.x1_var)
        self.y1_entry = Entry(self, textvariable=self.y1_var)

        self.x0_label.grid()
        self.x0_entry.grid()
        self.y0_label.grid()
        self.y0_entry.grid()
        self.x1_label.grid()
        self.x1_entry.grid()
        self.y1_label.grid()
        self.y1_entry.grid()

        self.bresenham_button = Button(
            self, text="Show Bresenham", command=self.show_bresenham
        )
        self.bresenham_button.grid()

        self.dda_button = Button(self, text="Show DDA", command=self.show_dda)
        self.dda_button.grid()

        self.clear_button = Button(self, text="Clear", command=self.clear)
        self.clear_button.grid()

    def show_bresenham(self):
        # Call the Bresenham algorithm and update your GUI
        x0 = int(self.x0_var.get())
        y0 = int(self.y0_var.get())
        x1 = int(self.x1_var.get())
        y1 = int(self.y1_var.get())
        pixels = bresenham(x0, y0, x1, y1)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="black"
            )

    def show_dda(self):
        x0 = int(self.x0_var.get())
        y0 = int(self.y0_var.get())
        x1 = int(self.x1_var.get())
        y1 = int(self.y1_var.get())
        pixels = dda(x0, y0, x1, y1)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="blue", outline="blue"
            )

    def clear(self):
        self.canvas.delete("all")