import numpy as np


def dda(x0, y0, x1, y1):
    """
    Implements the DDA (Digital Differential Analyzer) line algorithm.

    Args:
        x0 (float): The x-coordinate of the starting point.
        y0 (float): The y-coordinate of the starting point.
        x1 (float): The x-coordinate of the ending point.
        y1 (float): The y-coordinate of the ending point.

    Returns:
        list: A list of points representing the line.

    """
    points = []

    dx = x1 - x0
    dy = y1 - y0

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    x, y = x0, y0

    points.append((round(x), round(y)))
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))
    return points


def transform(x0, y0, x1, y1, transformation_matrix):
    """
    Translates the points (x0, y0) and (x1, y1) using a 3x3 transformation matrix.

    Args:
        x0 (float): The x-coordinate of the starting point.
        y0 (float): The y-coordinate of the starting point.
        x1 (float): The x-coordinate of the ending point.
        y1 (float): The y-coordinate of the ending point.
        transformation_matrix (numpy.ndarray): The 3x3 transformation matrix.

    Returns:
        tuple: A tuple containing the trasnformed points (x0t, y0t, x1t, y1t).

    """
    # Create homogeneous coordinates
    points = np.array([[x0, y0, 1], [x1, y1, 1]])

    # Apply translation matrix
    transformedPoints = [np.matmul(transformation_matrix, point) for point in points]

    # Extract translated coordinates
    x0t, y0t, _ = transformedPoints[0]
    x1t, y1t, _ = transformedPoints[1]

    # Cast translated points to integers
    x0t, y0t = int(x0t), int(y0t)
    x1t, y1t = int(x1t), int(y1t)

    return x0t, y0t, x1t, y1t


def rotateWithAngle(x0, y0, x1, y1, angle):
    """
    Rotates the points (x0, y0) and (x1, y1) by a given angle.

    Args:
        x0 (float): The x-coordinate of the starting point.
        y0 (float): The y-coordinate of the starting point.
        x1 (float): The x-coordinate of the ending point.
        y1 (float): The y-coordinate of the ending point.
        angle (float): The angle of rotation in degrees.

    Returns:
        tuple: A tuple containing the rotated points (x0r, y0r, x1r, y1r).

    """
    # Convert angle to radians
    angle = np.radians(angle)

    # Create rotation matrix
    transformation_matrix = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )

    return transform(x0, y0, x1, y1, transformation_matrix)


def offsetToOrigin(x0, y0, x1, y1):
    """
    Offsets the line to the origin.

    This method takes the coordinates of two points and offsets them to the origin (0, 0) by
    subtracting the x and y coordinates of the first point from both points. It then returns the
    new coordinates of the two points.

    Args:
        x0 (int): The x-coordinate of the first point.
        y0 (int): The y-coordinate of the first point.
        x1 (int): The x-coordinate of the second point.
        y1 (int): The y-coordinate of the second point.

    Returns:
        tuple: A tuple containing the new coordinates of the two points in the following order: x0, y0, x1, y1.
    """
    return x0 - x0, y0 - y0, x1 - x0, y1 - y0


def offsetFromOrigin(x0, y0, x1, y1, x, y):
    """
    Offsets the line from the origin.

    This method takes the coordinates of two points and offsets them from the origin (0, 0) by
    adding the x and y coordinates of the first point to both points. It then returns the
    new coordinates of the two points.

    Args:
        x0 (int): The x-coordinate of the first point.
        y0 (int): The y-coordinate of the first point.
        x1 (int): The x-coordinate of the second point.
        y1 (int): The y-coordinate of the second point.
        x (int): The x-coordinate of the origin.
        y (int): The y-coordinate of the origin.

    Returns:
        tuple: A tuple containing the new coordinates of the two points in the following order: x0, y0, x1, y1.
    """
    return x0 + x, y0 + y, x1 + x, y1 + y


def bresenham(x0, y0, x1, y1):
    """
    Implements the Bresenham's line algorithm to generate a list of points
    between two given points (x0, y0) and (x1, y1) in a 2D space.

    Args:
        x0 (int): The x-coordinate of the starting point.
        y0 (int): The y-coordinate of the starting point.
        x1 (int): The x-coordinate of the ending point.
        y1 (int): The y-coordinate of the ending point.

    Returns:
        list: A list of points representing the line between the two given points.

    """
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points.append((x, y))
    return points


def bresenhamCircle(x_center, y_center, r):
    """
    Generates a list of points that form a circle using the Bresenham's circle algorithm.

    Args:
        x_center (int): The x-coordinate of the center of the circle.
        y_center (int): The y-coordinate of the center of the circle.
        r (int): The radius of the circle.

    Returns:
        list: A list of points that form the circle.

    """
    points = []
    x, y = 0, r

    # Initial value of decision parameter
    d = 3 - 2 * r

    while x <= y:
        points.append((x_center + x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center + y))
        points.append((x_center - x, y_center - y))
        points.append((x_center + y, y_center + x))
        points.append((x_center + y, y_center - x))
        points.append((x_center - y, y_center + x))
        points.append((x_center - y, y_center - x))

        # update the value of decision parameter
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    return points


# Viewport / Line Clipping


def cohenSutherlandClip(x0, y0, x1, y1, x_min, y_min, x_max, y_max):
    """
    Implements the Cohen-Sutherland line clipping algorithm to clip a line from
    (x0, y0) to (x1, y1) against a rectangular viewport with the given boundaries.

    Args:
        x0 (int): The x-coordinate of the starting point.
        y0 (int): The y-coordinate of the starting point.
        x1 (int): The x-coordinate of the ending point.
        y1 (int): The y-coordinate of the ending point.
        x_min (int): The minimum x-coordinate of the viewport.
        y_min (int): The minimum y-coordinate of the viewport.
        x_max (int): The maximum x-coordinate of the viewport.
        y_max (int): The maximum y-coordinate of the viewport.

    Returns:
        tuple: A tuple containing the clipped points (x0, y0, x1, y1).

    """
    INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

    def computeCode(x, y):
        code = INSIDE
        if x < x_min:
            code |= LEFT
        elif x > x_max:
            code |= RIGHT
        if y < y_min:
            code |= BOTTOM
        elif y > y_max:
            code |= TOP
        return code

    code0, code1 = computeCode(x0, y0), computeCode(x1, y1)
    while True:
        if code0 == 0 and code1 == 0:
            return x0, y0, x1, y1
        elif code0 & code1:
            return None
        else:
            x, y = 0, 0
            code_out = code1 if code1 > code0 else code0
            if code_out & TOP:
                x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                y = y_max
            elif code_out & BOTTOM:
                x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
                y = y_min
            elif code_out & RIGHT:
                y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                x = x_max
            elif code_out & LEFT:
                y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                x = x_min
            if code_out == code0:
                x0, y0 = int(x), int(y)
                code0 = computeCode(x0, y0)
            else:
                x1, y1 = int(x), int(y)
                code1 = computeCode(x1, y1)


def liangBarskyClip(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    dx = x1 - x0
    dy = y1 - y0

    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    u1 = 0
    u2 = 1

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

        if u1 > u2:
            return None

    x0_clip = x0 + u1 * dx
    y0_clip = y0 + u1 * dy
    x1_clip = x0 + u2 * dx
    y1_clip = y0 + u2 * dy

    return x0_clip, y0_clip, x1_clip, y1_clip
