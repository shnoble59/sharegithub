"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730136744"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie()) 
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Selects a random number which gives you a random fortune (r)."""
    x = randint(1, 10)
    if x <= 2:
        r1: str = ("You will finish this semester with all As in your classes!")
        return r1
    else: 
        if x <= 4:
            r2: str = ("You will find succeess and happiness in life!")
            return r2
        else: 
            if x <= 6:
                r3: str = ("You will be proud of who you become!")
                return r3
            else:
                if x <= 8:
                    r4: str = ("You are destined to make a difference!")
                    return r4
                else:
                    r5: str = ("You will be someone people are proud to know!")
                    return r5


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
