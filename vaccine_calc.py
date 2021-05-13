"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730136744"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population, doses, doses_per_day, target)
    future: str = future_date(days)
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + future + ".")


def days_to_target(a: int, b: int, c: int, d: int) -> int: 
    """Defining days_to_target. entry point."""
    pop = a
    dos_a = b
    dos_pd = c
    target = d
    dec_target = target / 100
    target_people = int(round(dec_target * pop))
    done = dos_a // 2
    left_to_go = target_people - done
    if dos_a % 2 >= 1:
        left_to_go = left_to_go + 1
    doses_to_go = left_to_go * 2
    days_left_1 = doses_to_go // dos_pd 
    final_day = doses_to_go % dos_pd
    rounded_final_day = round(final_day)
    context = rounded_final_day / dos_pd
    if context >= 0.5:
        days_left_1 = days_left_1 + 1
    return(days_left_1)


def future_date(x: int) -> str: 
    """Defining future_date. entry point."""
    timeline: timedelta = timedelta(x)
    today: datetime = datetime.today()
    future: datetime = today + timeline
    the_day: str = future.strftime("%B %d, %Y")
    return(the_day) 


if __name__ == "__main__":
    main()
