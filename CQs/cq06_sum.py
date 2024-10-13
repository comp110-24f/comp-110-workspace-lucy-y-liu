"""Summing the elements of a list using different loops"""

__author__ = "730763566"


def w_sum(vals: list[float]) -> float:
    i: int = 0
    total: float = 0.0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for num in vals:
        total += num
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for num in range(0, len(vals)):
        total += vals[num]
    return total
