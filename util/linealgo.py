from decorators import timer


def signum(x):
    return 1 if x > 0 else -1 if x < 0 else 0


@timer
def bresenham(xstart, ystart, xend, yend):
    """
    Bresenham algorithm between points (xstart, ystart) and (xend, yend).
    :param xstart:
    :param ystart:
    :param xend:
    :param yend:
    :return: None
    """
    # Calculate distance in both dimensions
    dx = xend - xstart
    dy = yend - ystart

    # Determine sign of increment
    increment_x = signum(dx)
    increment_y = signum(dy)
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    # Determine which distance is greater
    if dx > dy:
        # x fast direction
        pdx, pdy = increment_x, 0      # step parallel
        ddx, ddy = increment_x, increment_y   # step diagonally
        delta_slow_direction, delta_fast_direction = dy, dx
    else:
        # y fast direction
        pdx, pdy = 0, increment_y      # step parallel
        ddx, ddy = increment_x, increment_y   # step diagonally
        delta_slow_direction, delta_fast_direction = dx, dy

    x = xstart
    y = ystart
    err = delta_fast_direction / 2
    connecting_path = [(x, y)]

    # Calculate pixel
    for t in range(delta_fast_direction):
        err -= delta_slow_direction
        if err < 0:
            err += delta_fast_direction
            x += ddx
            y += ddy
        else:
            x += pdx
            y += pdy
        connecting_path.append((x, y))

    return connecting_path


def main():
    assert signum(-4) == -1
    assert signum(0) == 0
    assert signum(-4567) == -1
    assert signum(1) == 1
    assert signum(-1) == -1
    assert signum(123123) == 1
    assert signum(6) == 1

    print(bresenham(0, 0, 7, 8))


if __name__ == "__main__":
    main()
