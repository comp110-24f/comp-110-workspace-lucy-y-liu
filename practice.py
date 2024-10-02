def sum(num1: int, num2: int) -> int:
    """adding num1 and num2 together"""
    return num1 + num2


def celsius_to_fahrenheit(degrees_c: int) -> float:
    """convert degrees celcius to degrees Fahrenheit"""
    return (degrees_c * 9 / 5) + 32


"""9/9/24 boolean expressions and if/else/then exercise"""


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        print("match")
        return letter
    else:
        print("no match")
        return letter


"""9/11/24 practice"""


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


grocery_list: list[str] = ["banannas", "milk"]

grocery_list.append("milk")

print(grocery_list)
