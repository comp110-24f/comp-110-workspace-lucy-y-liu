"""9/28/24 Wordle"""

__author__ = "730763566"


def input_guess(secret_word_len: int) -> str:
    """to check to see if the input is the correct length"""
    input_word: str = input(f"Enter a {str(secret_word_len)} character word: ")
    while len(input_word) != secret_word_len:
        input_word = input(f"That wasn't {str(secret_word_len)} chars! Try again: ")
    return input_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    # making sure that it errors if char_guess isn't 1 length long
    """A function to check to see if there are any shared characters"""
    index: int = 0  # used to loop through secret_word
    evaluation: bool = False
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            evaluation = True
        index += 1
    return evaluation


def emojified(guess: str, secret: str) -> str:
    """Displays results in emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index: int = 0
    result: str = ""

    while index < len(secret):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]) is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guess: str = ""
    turn: int = 1
    win: bool = False
    length: int = len(secret)  # length of the secret word
    GREEN_BOX: str = "\U0001F7E9"  # in order to check to see if the game has won.

    while turn <= 6 and win is False:  # conditions to keep playing
        print(f"=== Turn {str(turn)}/6 ===")  # The format of the turns
        result: str = emojified(guess=input_guess(length), secret=secret)
        print(result)
        if result == (GREEN_BOX * length):
            win = True
        else:
            turn += 1

    if turn > 6:
        print(f"X/6 - Sorry try again tomorrow!")
    elif win is True:
        print(f"You won in {turn}/6 turns!")


if __name__ == "__main__":
    main(secret="codes")
