"""EX03 - avoid_fifth function."""

__author__: str = "730136744"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello my dears. Envelope."))
    print(avoid_fifth("baFDBfCbdaFbbCfbdcdCdcbcDfAdcffcdfCAbaBAcFFbfCEdaFCdAdaCaaffdfcABacaDDDcACdAabdcBaAfBcB"))
    print(avoid_fifth("taaaaaar heeels!"))
    print(avoid_fifth("TAAAAAAR HEEELS!"))
    print(avoid_fifth("TAR HEEEEEEEEEEELSSSSS!!!"))


def avoid_fifth(sent: str) -> str:
    """Taking out all the e and Es in the sentance!"""
    i = 0
    new: str = sent
    while i < len(new):
        if new[i] == 'e':
            new = new[:i] + new[i + 1:]
        elif new[i] == 'E':
            new = new[:i] + new[i + 1:]
        if new[i - 1] == 'e':
            new = new[:i - 1] + new[i:]
        elif new[i - 1] == 'E':
            new = new[:i - 1] + new[i:]
        i += 1
    k = 0
    while k < len(new):     # and again for good measure
        if new[k] == 'e':
            new = new[:k] + new[k + 1:]
        elif new[k] == 'E':
            new = new[:k] + new[k + 1:]
        if new[k - 1] == 'e':
            new = new[:k - 1] + new[k:]
        elif new[k - 1] == 'E':
            new = new[:k - 1] + new[k:]
        k += 1        # extra to cover skipped spots due to length change in str
    return(new)


if __name__ == "__main__":
    main()