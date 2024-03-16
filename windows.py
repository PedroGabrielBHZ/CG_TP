from tkinter import Frame, Button, Canvas, Entry, StringVar, Label
from algorithms import bresenham, bresenham_circle, dda

pixel_size = 2


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.setting_viewport = False
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and configures the widgets for the graphical user interface.

        This method creates and configures various widgets such as canvas, labels, entry fields, and buttons
        for the graphical user interface. It sets up the layout and positioning of these widgets using the grid system.

        Args:
            self: The object instance.

        Returns:
            None
        """
        self.canvas = Canvas(self, width=800, height=600, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Viewport
        self.vx0_var = StringVar()
        self.vx0_label = Label(self, text="vx0:")
        self.vx0_entry = Entry(self, textvariable=self.vx0_var)
        self.vx0_label.grid()
        self.vx0_entry.grid()

        self.vy0_var = StringVar()
        self.vy0_label = Label(self, text="vy0:")
        self.vy0_entry = Entry(self, textvariable=self.vy0_var)
        self.vy0_label.grid()
        self.vy0_entry.grid()

        self.vx1_var = StringVar()
        self.vx1_label = Label(self, text="vx1:")
        self.vx1_entry = Entry(self, textvariable=self.vx1_var)
        self.vx1_label.grid()
        self.vx1_entry.grid()

        self.vy1_var = StringVar()
        self.vy1_label = Label(self, text="vy1:")
        self.vy1_entry = Entry(self, textvariable=self.vy1_var)
        self.vy1_label.grid()
        self.vy1_entry.grid()

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

        # Set Viewport Button
        self.set_viewport_button = Button(
            self, text="Set Viewport", command=self.set_viewport
        )
        self.set_viewport_button.grid(row=5, column=1)

        # Clear Button
        self.clear_button = Button(self, text="Clear", command=self.clear)
        self.clear_button.grid(column=1, row=2)

    def show_bresenham(self):
        """
        Draws a line using the Bresenham's line algorithm.

        This method calculates the pixels that form a line between two given points
        using the Bresenham's line algorithm. It then draws rectangles on the canvas
        to represent the pixels of the line.

        Parameters:
            None

        Returns:
            None
        """
        x0, y0, x1, y1 = self.getPoints()
        pixels = bresenham(x0, y0, x1, y1)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="black"
            )

    def show_dda(self):
        """
        Draws a line using the DDA (Digital Differential Analyzer) algorithm.

        This method calculates the pixels that form a line between two given points
        using the DDA algorithm. It then draws rectangles on a canvas to represent
        each pixel of the line.

        Returns:
            None
        """
        x0, y0, x1, y1 = self.getPoints()
        pixels = dda(x0, y0, x1, y1)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="blue", outline="blue"
            )

    def show_bresenham_circle(self):
        """
        Draws a circle using the Bresenham's algorithm.

        This method calculates the parameters of the circle (center coordinates and radius)
        and then uses the Bresenham's algorithm to generate the pixels that form the circle.
        Each pixel is then drawn on the canvas as a black rectangle.

        Returns:
            None
        """
        x_center, y_center, r = self.get_circle_parameters()
        pixels = bresenham_circle(x_center, y_center, r)
        for pixel in pixels:
            x, y = pixel
            self.canvas.create_rectangle(
                x, y, x + pixel_size, y + pixel_size, fill="black"
            )

    def get_circle_parameters(self):
        """
        Get the parameters of a circle.

        Returns:
            Tuple[int, int, int]: The x and y coordinates of the center of the circle, and the radius.
        """
        x_center = int(self.x0_var.get())
        y_center = int(self.y0_var.get())
        r = int(self.x1_var.get())
        return x_center, y_center, r

    def getPoints(self):
        """
        Get the x and y coordinates of two points.

        Returns:
            tuple: A tuple containing the x and y coordinates of two points in the following order: x0, y0, x1, y1.
        """
        x0 = int(self.x0_var.get())
        y0 = int(self.y0_var.get())
        x1 = int(self.x1_var.get())
        y1 = int(self.y1_var.get())
        return x0, y0, x1, y1

    def getViewport(self):
        """
        Get the viewport coordinates.

        Returns:
            A tuple containing the x and y coordinates of the top-left corner (vx0, vy0)
            and the x and y coordinates of the bottom-right corner (vx1, vy1) of the viewport.
        """
        vx0 = int(self.vx0_var.get())
        vy0 = int(self.vy0_var.get())
        vx1 = int(self.vx1_var.get())
        vy1 = int(self.vy1_var.get())
        return vx0, vy0, vx1, vy1

    def on_canvas_click(self, event):
        """
        Handle the click event on the canvas.

        If the setting_viewport flag is True, the method sets the viewport coordinates
        based on the click event. If the vx0 and vy0 variables are not set, they are
        set to the coordinates of the click. If the vx0 and vy0 variables are set, but
        vx1 and vy1 are not, vx1 and vy1 are set. If all variables are set, all of them
        are reset.

        If the setting_viewport flag is False, the method sets the coordinates of the
        click event to the x0 and y0 variables if they are not set. If x0 and y0 are set,
        but x1 and y1 are not, x1 and y1 are set. If all variables are set, all of them
        are reset.
        """
        if self.setting_viewport:
            # If vx0 and vy0 are not set, set them to the coordinates of the click
            if not self.vx0_var.get() and not self.vy0_var.get():
                self.vx0_var.set(event.x)
                self.vy0_var.set(event.y)

            # If vx0 and vy0 are set, but vx1 and vy1 are not, set vx1 and vy1
            elif not self.vx1_var.get() and not self.vy1_var.get():
                self.vx1_var.set(event.x)
                self.vy1_var.set(event.y)

            # If all variables are set, reset all of them
            else:
                self.vx0_var.set("")
                self.vy0_var.set("")
                self.vx1_var.set("")
                self.vy1_var.set("")

            return

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

    def set_viewport(self):
        """
        Toggles the viewport setting mode.

        If the viewport setting mode is currently active, it will be deactivated and the text of the
        set_viewport_button will be set to "Set Viewport". If the viewport setting mode is currently
        inactive, it will be activated and the text of the set_viewport_button will be set to
        "Cancel Set Viewport".
        """
        if self.setting_viewport:
            self.setting_viewport = False
            self.set_viewport_button.config(text="Set Viewport")
        else:
            self.setting_viewport = True
            self.set_viewport_button.config(text="Cancel Set Viewport")

    def clear(self):
        """
        Clears the canvas by deleting all items.
        """
        self.canvas.delete("all")
