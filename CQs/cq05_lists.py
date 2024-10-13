"""Mutating functions"""

__author__ = "730763566"


def manual_append(input1: list[int], input2: int) -> None:
    """adding input2 to the list"""
    input1.append(input2)  # adding input 2 to the end of input1


def double(input1: list[int]) -> None:
    """doubling input 1 list items"""
    index: int = 0
    while index < len(input1):
        input1[index] = input1[index] * 2  # doubling input1 values
        index += 1  # in order to end the while loop eventually


list1: list[int] = [1, 2, 3]
list2: list[int] = list1

double(list2)
print(list1)
print(list2)
# i think that list 1 and list 2 will both be doubled [2,4,6]
