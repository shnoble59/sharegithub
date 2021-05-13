"""EX03 - prime functions."""

__author__: str = "730136744"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(5))
    print(is_prime(31))
    print(is_prime(14034))
    print(is_prime(-10))
    print(list_primes(1, 20))
    print(list_primes(10, 30))
    print(list_primes(3, 7))
    print(list_primes(1, 100))

   
def is_prime(x: int) -> bool:
    """Checking to see if my number input is prime!"""
    if x == 1 or x == 0 or x < 0:
        return(False)
    i = x - 1
    j = 1
    while i > j:
        if x % i == 0:
            return(False)
        else:
            i -= 1
    return(True)


def list_primes(x: int, y: int) -> list[int]:
    """Taking a range returns list of all prime numbers in it."""
    if y > x:
        b = y
        a = x
    else:
        b = x
        a = y 
    primes_in_range: list[int] = []
    c = b - 1
    while c >= a:
        cond = is_prime(c)
        if cond is True:
            primes_in_range.append(c)  
            c -= 1
        else:
            c -= 1
    primes_in_range.reverse()
    return(primes_in_range)


if __name__ == "__main__":
    main()