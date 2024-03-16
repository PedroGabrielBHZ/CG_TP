# algorithms.py


def dda(x0, y0, x1, y1):
    # DDA line algorithm
    points = []

    # distance between points
    dx = x1 - x0
    dy = y1 - y0

    # number of steps gets decided by the bigger of variations
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # if dx is bigger, x_increment equals 1, otherwise y_increment equals 1
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    x, y = x0, y0

    # start populating point vector
    points.append((round(x), round(y)))
    for _ in range(steps):
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


def bresenham_circle(xc, yc, r):
    # Bresenham's circle algorithm
    points = []
    x, y = 0, r
    d = 3 - 2 * r
    while x <= y:
        points.append((xc + x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc + y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc + x))
        points.append((xc - y, yc - x))
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    return points
