"""10/13/24"""

__author__ = "760763566"


def all(input: list[int], num: int) -> bool:
    result: bool = True  # return variable
    for x in input:  # looping to see if num isn't equal to x
        if x != num:
            result = False
    if len(input) == 0:  # if there's an empty list
        result = False

    return result


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = 0  # starting max
    for x in input:  # looping to find the max by comparison
        if x > max:
            max = x
    return max


def is_equal(input1: list[int], input2: list[int]) -> bool:
    result: bool = True  # starting result variable
    if len(input1) != len(input2):  # making sure lengths are the same
        result = False
    else:
        for i in range(0, len(input1)):  # looping index with range
            if input1[i] != input2[i]:  # if the lists are equal
                result = False
    return result


def extend(list1: list[int], list2: list[int]) -> None:
    for x in list2:  # only adding the second list to the first list
        list1.append(x)
    print(list1)
