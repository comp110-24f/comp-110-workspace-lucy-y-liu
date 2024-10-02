"""Coordinates 9/27/24"""

__author__ = "730763566"


def get_coords(xs: str, ys: str) -> None:
    yindex: int = 0
    xindex: int = 0
    coord: str = ""
    newcoord: str = ""
    x: str = ""
    y: str = ""
    while xindex < len(xs):
        x = xs[xindex]
        coord = "(" + x + ","
        xindex += 1
        yindex = 0
        while yindex < len(ys):
            y = ys[yindex]
            newcoord = coord + y + ")"
            print(newcoord)
            newcoord = ""
            yindex += 1
