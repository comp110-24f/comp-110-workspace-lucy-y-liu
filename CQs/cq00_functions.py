"""8/28/24"""

__author__ = "730763566"


def mimic(message: str) -> str:
    """ "Repeteating the message back to you"""
    return message


def main() -> None:
    """printing the result of mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
