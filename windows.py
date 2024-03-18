from tkinter import *
from tkinter import messagebox

from algorithms import *
import numpy as np

pixel_size = 1


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
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Viewport
        self.vx0_var = IntVar()
        self.vx0_label = Label(self, text="vx0:")
        self.vx0_entry = Entry(self, textvariable=self.vx0_var)
        self.vx0_label.grid(row=1, column=0)
        self.vx0_entry.grid(row=1, column=1)

        self.vy0_var = IntVar()
        self.vy0_label = Label(self, text="vy0:")
        self.vy0_entry = Entry(self, textvariable=self.vy0_var)
        self.vy0_label.grid(row=2, column=0)
        self.vy0_entry.grid(row=2, column=1)

        self.vx1_var = IntVar()
        self.vx1_label = Label(self, text="vx1:")
        self.vx1_entry = Entry(self, textvariable=self.vx1_var)
        self.vx1_label.grid(row=3, column=0)
        self.vx1_entry.grid(row=3, column=1)

        # Entry widgets
        self.vy1_var = IntVar()
        self.vy1_label = Label(self, text="vy1:")
        self.vy1_entry = Entry(self, textvariable=self.vy1_var)
        self.vy1_label.grid(row=4, column=0)
        self.vy1_entry.grid(row=4, column=1)

        self.x0_var = IntVar()
        self.x0_label = Label(self, text="Line's first X coordinate:")
        self.x0_entry = Entry(self, textvariable=self.x0_var)
        self.x0_label.grid(row=5, column=0)
        self.x0_entry.grid(row=5, column=1)

        self.y0_var = IntVar()
        self.y0_label = Label(self, text="Line's first Y coordinate:")
        self.y0_entry = Entry(self, textvariable=self.y0_var)
        self.y0_label.grid(row=6, column=0)
        self.y0_entry.grid(row=6, column=1)

        self.x1_var = IntVar()
        self.x1_label = Label(self, text="Line's second X coordinate:")
        self.x1_entry = Entry(self, textvariable=self.x1_var)
        self.x1_label.grid(row=7, column=0)
        self.x1_entry.grid(row=7, column=1)

        self.y1_var = IntVar()
        self.y1_label = Label(self, text="Line's second Y coordinate:")
        self.y1_entry = Entry(self, textvariable=self.y1_var)
        self.y1_label.grid(row=8, column=0)
        self.y1_entry.grid(row=8, column=1)

        # Transformation matrix
        self.empty_label = Label(self, text="Transformation Matrix")
        self.empty_label.grid(row=11, column=0, columnspan=3)

        self.m0_var = IntVar()
        self.m0_var.set("1")
        self.m0_entry = Entry(self, textvariable=self.m0_var)
        self.m0_entry.grid(row=12, column=0)

        self.m1_var = IntVar()
        self.m1_var.set("0")
        self.m1_entry = Entry(self, textvariable=self.m1_var)
        self.m1_entry.grid(row=12, column=1)

        self.m2_var = IntVar()
        self.m2_var.set("0")
        self.m2_entry = Entry(self, textvariable=self.m2_var)
        self.m2_entry.grid(row=12, column=2)

        self.m3_var = IntVar()
        self.m3_var.set("0")
        self.m3_entry = Entry(self, textvariable=self.m3_var)
        self.m3_entry.grid(row=13, column=0)

        self.m4_var = IntVar()
        self.m4_var.set("1")
        self.m4_entry = Entry(self, textvariable=self.m4_var)
        self.m4_entry.grid(row=13, column=1)

        self.m5_var = IntVar()
        self.m5_var.set("0")
        self.m5_entry = Entry(self, textvariable=self.m5_var)
        self.m5_entry.grid(row=13, column=2)

        self.m6_var = IntVar()
        self.m6_var.set("0")
        self.m6_entry = Entry(self, textvariable=self.m6_var)
        self.m6_entry.grid(row=14, column=0)

        self.m7_var = IntVar()
        self.m7_var.set("0")
        self.m7_entry = Entry(self, textvariable=self.m7_var)
        self.m7_entry.grid(row=14, column=1)

        self.m8_var = IntVar()
        self.m8_var.set("1")
        self.m8_entry = Entry(self, textvariable=self.m8_var)
        self.m8_entry.grid(row=14, column=2)

        # Bresenham Button
        self.bresenham_button = Button(
            self, text="Show Bresenham", command=self.showBresenham, bd=5, width=20
        )
        self.bresenham_button.grid(column=2, row=1)

        # DDA Button
        self.dda_button = Button(
            self, text="Show DDA", command=self.showDDA, bd=5, width=20
        )
        self.dda_button.grid(column=2, row=2)

        # Bresenham Circle Button
        self.bresenham_circle_button = Button(
            self,
            text="Show Bresenham Circle",
            command=self.displayBresenhamCircle,
            bd=5,
            width=20,
        )
        self.bresenham_circle_button.grid(row=3, column=2)

        # Set Viewport Button
        self.set_viewport_button = Button(
            self,
            text="Set Viewport",
            command=self.setViewport,
            bg="blue",
            fg="white",
            bd=5,
            width=20,
        )
        self.set_viewport_button.grid(row=4, column=2)

        # Cohen-Sutherland Clipping Button
        self.clip_button = Button(
            self,
            text="Cohen-Sutherland Clipping",
            command=self.displayBresenhamCut,
            bd=5,
            width=20,
        )
        self.clip_button.grid(row=5, column=2)

        # Liang-Barsky Clipping Button
        self.clip_button = Button(
            self,
            text="Liang-Barsky Clipping",
            command=self.displayLiangBarskyCut,
            bd=5,
            width=20,
        )
        self.clip_button.grid(row=6, column=2)

        # Clear Button
        self.clear_button = Button(
            self, text="Clear", command=self.clear, bd=5, bg="red", fg="white", width=20
        )
        self.clear_button.grid(row=7, column=2)

        # Translation Button
        self.translation_button = Button(
            self,
            text="Transform",
            command=self.transform,
            bd=5,
            width=20,
        )
        self.translation_button.grid(row=1, column=3)

        # Rotation Button
        self.rotation_button = Button(
            self,
            text="Rotate with angle",
            command=self.rotate,
            bd=5,
            width=20,
        )
        self.rotation_button.grid(row=2, column=3)

        # Angle input
        self.angle_var = IntVar()
        self.angle_label = Label(self, text="Angle:")
        self.angle_entry = Entry(self, textvariable=self.angle_var)
        self.angle_label.grid(row=3, column=3)
        self.angle_entry.grid(row=4, column=3)

        # Circle radius input
        self.radius_var = IntVar()
        self.radius_label = Label(self, text="Radius:")
        self.radius_entry = Entry(self, textvariable=self.radius_var)
        self.radius_label.grid(row=5, column=3)
        self.radius_entry.grid(row=6, column=3)

        # Display greeting message
        messagebox.showinfo(
            "Welcome",
            "Welcome to the Computer Graphics Showcase!\n\nClick on the canvas to set the line's coordinates or the viewport's corners.\n\nUse the buttons to display the line, circle, or to perform transformations.",
        )

    def rotate(self):
        """
        Performs a geometric transformation on the line.

        This method performs a geometric transformation on the line using the transformation matrix
        entered by the user. It then draws the transformed line on the canvas.

        Raises:
            Exception: If an error occurs during the transformation process.

        Returns:
            None
        """
        try:
            x0, y0, x1, y1 = self.getPoints()

            # offset to origin
            x0t, y0t, x1t, y1t = offsetToOrigin(x0, y0, x1, y1)

            # fetch rotation angle
            angle = float(self.angle_var.get())

            # rotate
            x0t, y0t, x1t, y1t = rotateWithAngle(x0t, y0t, x1t, y1t, angle)

            # translate back to original position
            x0t, y0t, x1t, y1t = offsetFromOrigin(x0t, y0t, x1t, y1t, x0, y0)

            # set new points
            self.x0_var.set(x0t)
            self.y0_var.set(y0t)
            self.x1_var.set(x1t)
            self.y1_var.set(y1t)

            # clear canvas
            self.canvas.delete("all")

            pixels = bresenham(x0t, y0t, x1t, y1t)
            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="green"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transform(self):
        """
        Performs a geometric transformation on the line.

        This method performs a geometric transformation on the line using the transformation matrix
        entered by the user. It then draws the transformed line on the canvas.

        Raises:
            Exception: If an error occurs during the transformation process.

        Returns:
            None
        """
        try:
            x0, y0, x1, y1 = self.getPoints()
            transformation_matrix = self.getTransformationMatrix()

            # offset to origin
            x0t, y0t, x1t, y1t = offsetToOrigin(x0, y0, x1, y1)

            # transform
            x0t, y0t, x1t, y1t = transform(x0t, y0t, x1t, y1t, transformation_matrix)

            # translate back to original position
            x0t, y0t, x1t, y1t = offsetFromOrigin(x0t, y0t, x1t, y1t, x0, y0)

            # set new points
            self.x0_var.set(x0t)
            self.y0_var.set(y0t)
            self.x1_var.set(x1t)
            self.y1_var.set(y1t)

            # clear canvas
            self.canvas.delete("all")

            pixels = bresenham(x0t, y0t, x1t, y1t)
            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="green"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def showBresenham(self):
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
        try:
            x0, y0, x1, y1 = self.getPoints()
            pixels = bresenham(x0, y0, x1, y1)
            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="black"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def showDDA(self):
        """
        Draws a line using the DDA (Digital Differential Analyzer) algorithm.

        This method calculates the pixels that form a line between two given points
        using the DDA algorithm. It then draws rectangles on a canvas to represent
        each pixel of the line.

        Returns:
            None
        """
        try:
            x0, y0, x1, y1 = self.getPoints()
            pixels = dda(x0, y0, x1, y1)
            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="blue", outline="blue"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def displayBresenhamCircle(self):
        """
        Draws a circle using the Bresenham's algorithm.

        This method calculates the parameters of the circle (center coordinates and radius)
        and then uses the Bresenham's algorithm to generate the pixels that form the circle.
        Each pixel is then drawn on the canvas as a black rectangle.

        Returns:
            None
        """
        try:
            x_center, y_center, r = self.getCircleParameters()
            pixels = bresenhamCircle(x_center, y_center, r)
            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="green", outline="green"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def getCircleParameters(self):
        """
        Get the parameters of a circle.

        Returns:
            Tuple[int, int, int]: The x and y coordinates of the center of the circle, and the radius.
        """
        x_center = int(self.x0_var.get())
        y_center = int(self.y0_var.get())
        r = int(self.radius_var.get())
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

    def getTransformationMatrix(self):
        """
        Get the transformation matrix.

        Returns:
            numpy.ndarray: A 3x3 matrix representing the transformation matrix.
        """
        m0 = float(self.m0_var.get())
        m1 = float(self.m1_var.get())
        m2 = float(self.m2_var.get())
        m3 = float(self.m3_var.get())
        m4 = float(self.m4_var.get())
        m5 = float(self.m5_var.get())
        m6 = float(self.m6_var.get())
        m7 = float(self.m7_var.get())
        m8 = float(self.m8_var.get())
        return np.array([[m0, m1, m2], [m3, m4, m5], [m6, m7, m8]])

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

    def displayBresenhamCut(self):
        """
        Clips a line using the Cohen-Sutherland algorithm.

        This method calculates the pixels that form a line between two given points
        using the Cohen-Sutherland algorithm. It then draws rectangles on the canvas
        to represent the pixels of the line.

        Returns:
            None
        """
        try:
            x0, y0, x1, y1 = self.getPoints()
            vx0, vy0, vx1, vy1 = self.getViewport()
            x0, y0, x1, y1 = cohenSutherlandClip(x0, y0, x1, y1, vx0, vy0, vx1, vy1)
            pixels = bresenham(x0, y0, x1, y1)

            # clear canvas
            self.canvas.delete("all")

            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="red"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def displayLiangBarskyCut(self):
        """
        Clips a line using the Liang-Barsky algorithm.

        This method calculates the pixels that form a line between two given points
        using the Liang-Barsky algorithm. It then draws rectangles on the canvas
        to represent the pixels of the line.

        Returns:
            None
        """
        try:
            x0, y0, x1, y1 = self.getPoints()
            vx0, vy0, vx1, vy1 = self.getViewport()
            result = liangBarskyClip(x0, y0, x1, y1, vx0, vy0, vx1, vy1)
            if result != None:
                x0, y0, x1, y1 = result
            # if result is none, throw exception
            else:
                raise Exception("Line is outside the viewport")

            # clear canvas
            self.canvas.delete("all")

            pixels = bresenham(x0, y0, x1, y1)
            for pixel in pixels:
                x, y = pixel
                self.canvas.create_rectangle(
                    x, y, x + pixel_size, y + pixel_size, fill="red"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

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
                self.vx0_var.set(0)
                self.vy0_var.set(0)
                self.vx1_var.set(0)
                self.vy1_var.set(0)

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
            self.x0_var.set(0)
            self.y0_var.set(0)
            self.x1_var.set(0)
            self.y1_var.set(0)

    def setViewport(self):
        """
        Toggles the viewport setting mode.

        If the viewport setting mode is currently active, it will be deactivated and the text of the
        set_viewport_button will be set to "Set Viewport". If the viewport setting mode is currently
        inactive, it will be activated and the text of the set_viewport_button will be set to
        "Cancel Set Viewport".
        """
        if self.setting_viewport:
            self.setting_viewport = False
            self.set_viewport_button.config(text="Set Viewport", bg="blue")
        else:
            self.setting_viewport = True
            self.set_viewport_button.config(text="Cancel Set Viewport", bg="red")

            # flash instructions
            messagebox.showinfo(
                "Set Viewport",
                "Click on the canvas to set the top-left and bottom-right corners of the viewport.\n\nClick the 'Set Viewport' button again to cancel.",
            )

    def clear(self):
        """
        Clears the canvas by deleting all items.
        """
        self.canvas.delete("all")
