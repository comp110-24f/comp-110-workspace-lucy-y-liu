"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730763566"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")  # input of the word here
    if (
        len(word) != 5
    ):  # figuring out if it doesn't work out first. If it works, it doesn't return a print()
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    index: int = 0  # index that loops through the word
    print("Searching for " + letter + " in " + word)
    count: int = 0  # number that keeps track of the how many instances there are
    while index < 5:
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count += 1  # have to update within the ifs
            index += 1
        else:
            index += 1  # it still updates regardless of the condition

    if count == 0:
        print(
            "No instances of " + letter + " found in " + word
        )  # seperate if statement for the count
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    elif count >= 2:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
