"""Utility functions for wrangling data."""

__author__ = "730136744"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    # 0.1) Complete the implementation of this function here.
    # add each row of data to our table
    for row in csv_reader:
        rows.append(row)
    # when we are done reading/ working with a file, close it!
    file_handle.close()
    print(rows)
    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    column_build: list[str] = []
    for row in table:
        column_build.append(str(row[column]))
    return column_build 


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    new_table: dict[str, list[str]] = {}
    column_names = table[0].keys()
    for key in column_names:
        take = key
        new_table[f"{take}"] = list(column_values(table, take))
    return new_table


def head(data: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column.""" 
    dict_build: dict[str, list[str]] = {}
    for column in data:
        first_n: list[str] = []
        x = 0
        while x < num and x < len(data[column]):
            first_n.append(data[column][x]) 
            x += 1
        dict_build[column] = first_n 
    return dict_build


def select(data: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    chosen_dict: dict[str, list[str]] = {}
    for item in copy:
        for column in data:
            if column == item:
                chosen_dict[column] = data[column]
    return chosen_dict


def count(values: list[str]) -> dict[str, int]:
    """Produce a dict where each key is a unique value in the given list and each value associated is the count."""
    dict_build: dict[str, int] = {}
    for item in values:
        dict_build[item] = 0
    for item in values:
        if item in dict_build:
            dict_build[item] = dict_build[item] + 1
        else:
            dict_build[item] = 1
    return dict_build
