# windows.py
from tkinter import Frame, Button, Canvas, Entry, StringVar, Label
from algorithms import bresenham, bresenham_circle, dda

pixel_size = 2


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, width=800, height=600, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Entry widgets
        self.x0_var = StringVar()
        self.x0_label = Label(self, text="x0:")
        self.x0_entry = Entry(self, textvariable=self.x0_var)
        self.x0_label.grid()
        self.x0_entry.grid()

        self.y0_var = StringVar()
        self.y0_label = Label(self, text="y0:")
        self.y0_entry = Entry(self, textvariable=self.y0_var)
        self.y0_label.grid()
        self.y0_entry.grid()

        self.x1_var = StringVar()
        self.x1_label = Label(self, text="x1:")
        self.x1_entry = Entry(self, textvariable=self.x1_var)
        self.x1_label.grid()
        self.x1_entry.grid()

        self.y1_var = StringVar()
        self.y1_label = Label(self, text="y1:")

        self.y1_entry = Entry(self, textvariable=self.y1_var)
        self.y1_label.grid()
        self.y1_entry.grid()

        # Bresenham Button
        self.bresenham_button = Button(
            self, text="Show Bresenham", command=self.show_bresenham
        )
        self.bresenham_button.grid(column=1, row=0)

        # DDA Button
        self.dda_button = Button(self, text="Show DDA", command=self.show_dda)
        self.dda_button.grid(column=1, row=1)

        # Bresenham Circle Button
        self.bresenham_circle_button = Button(
            self, text="Show Bresenham Circle", command=self.show_bresenham_circle
        )
        self.bresenham_circle_button.grid(row=3, column=1)

        # Clear Button
        self.clear_button = Button(self, text="Clear", command=self.clear)
        self.clear_button.grid(column=1, row=2)

    def show_bresenham(self):
        x0, y0, x1, y1 = self.getPoints()
        pixels = bresenham(x0, y0, x1, y1)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="black"
            )

    def show_dda(self):
        x0, y0, x1, y1 = self.getPoints()
        pixels = dda(x0, y0, x1, y1)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="blue", outline="blue"
            )

    def show_bresenham_circle(self):
        x_center, y_center, r = self.get_circle_parameters()
        pixels = bresenham_circle(x_center, y_center, r)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="black"
            )

    def get_circle_parameters(self):
        x_center = int(self.x0_var.get())
        y_center = int(self.y0_var.get())
        r = int(self.x1_var.get())
        return x_center, y_center, r

    def getPoints(self):
        x0 = int(self.x0_var.get())
        y0 = int(self.y0_var.get())
        x1 = int(self.x1_var.get())
        y1 = int(self.y1_var.get())
        return x0, y0, x1, y1

    def on_canvas_click(self, event):
        # If x0 and y0 are not set, set them to the coordinates of the click
        if not self.x0_var.get() and not self.y0_var.get():
            self.x0_var.set(event.x)
            self.y0_var.set(event.y)
        # If x0 and y0 are set, but x1 and y1 are not, set x1 and y1
        elif not self.x1_var.get() and not self.y1_var.get():
            self.x1_var.set(event.x)
            self.y1_var.set(event.y)
        # If all variables are set, reset all of them
        else:
            self.x0_var.set("")
            self.y0_var.set("")
            self.x1_var.set("")
            self.y1_var.set("")

    def clear(self):
        self.canvas.delete("all")
