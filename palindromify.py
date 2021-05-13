"""EX03 - palindromify function."""

__author__: str = "730136744"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    # True for even, False for odd
    print(palindromify("race", False))
    print(palindromify("live on time ", False))
    print(palindromify("red", True))


def palindromify(x: str, yn: bool) -> str:
    """Takes the word and mirrors in either even or odd style palindromes --> returns it."""
    i = len(x) - 1
    j = 0
    palin = ""
    cond = yn
    if cond is True:
        while i >= j:
            palin += x[i]
            i -= 1
        return(x + palin)
    elif cond is False:
        i -= 1
        while i >= j:
            palin += x[i]
            i -= 1
        return(x + palin)
    else:
        return("something is wrong")


if __name__ == "__main__":
    main()