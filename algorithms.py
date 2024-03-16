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
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    return points
