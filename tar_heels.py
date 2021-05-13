"""Tar Heels exercise redux as a structured program."""

__author__ = "730136744"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    num = choice
    print(tar_heels(num))


def tar_heels(num: int) -> str:
    """Defining the function!"""
    x = num 
    a: int = x % 2
    b: int = x % 7
    if a <= 0:
        if b <= 0:
            return("TAR HEELS")
        else:
            return("TAR")
    else:
        if b <= 0:
            return("HEELS")
        else:
            return("CAROLINA")


if __name__ == "__main__":
    main()
