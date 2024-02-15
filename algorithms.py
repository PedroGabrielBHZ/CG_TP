# algorithms.py


def dda(x0, y0, x1, y1):
    # DDA line algorithm
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    x, y = x0, y0
    points.append((round(x), round(y)))
    for k in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))
    return points


def bresenham(x0, y0, x1, y1):
    # Bresenham's line algorithm
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
