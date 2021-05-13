"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730136744"


class Simpy:
    """Making my simpy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initializing my dear Simpy."""
        self.values = values
    
    def __repr__(self) -> str:
        """Making it print in a way that makes sense to us."""
        return f"Simpy({self.values})"

    def fill(self, fillingfloat: float, fillingint: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        newval: list[float] = []
        for i in range(0, fillingint):
            newval.append(fillingfloat)
        self.values = newval
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        assert step != 0.0
        stepit: list[float] = [] 
        x = start
        if step < 0: 
            while x > stop:
                stepit.append(x)
                x += step
        else:
            while x < stop: 
                stepit.append(x)
                x += step
        self.values = stepit
    
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        x = sum(self.values) 
        return(x)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add the ability to use the addition operator (+)."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values: 
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result) 

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add the ability to use the power operator (**)."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values: 
                new = item 
                y = int(rhs)
                if rhs == 0:
                    new = 1.0
                else:
                    for i in range(0, y - 1): 
                        new *= item
                result.append(new)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                orig = self.values[i]
                new = self.values[i]
                y = int(rhs.values[i])
                if rhs.values[i] == 0:
                    new = 1.0
                else:
                    for a in range(0, y - 1): 
                        new *= orig                
                result.append(new)
        return Simpy(result)
    
    def __mod__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add the ability to use the modulus/remainder operator (%)."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values: 
                x = item / rhs 
                if x < 1 and x > 0:
                    result.append(item)
                elif x == round(x):
                    result.append(0.0)
                else:
                    if x > round(x):
                        new = item - round(x) * rhs
                        result.append(new)
                    else:
                        new = item - (round(x) - 1) * rhs
                        result.append(new)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new = self.values[i]
                rhsi = rhs.values[i]
                x = new / rhsi
                if x < 1 and x > 0:
                    result.append(new)
                elif x == round(x):
                    result.append(0.0)
                else:
                    if x > round(x):
                        new = new - round(x) * rhsi
                        result.append(new)
                    else:
                        new = new - (round(x) - 1) * rhsi
                        result.append(new)
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produce a mask with equality to other Simpy or Float."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values: 
                result.append(item == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result 

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produce a mask with grerater than other Simpy or Float."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values: 
                result.append(item > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result 

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Working the mask with self: either two Simpys or a Simpy and a float."""
        if isinstance(rhs, int):
            return(self.values[rhs])
        else:
            result: list[float] = [] 
            assert len(self.values) == len(rhs)
            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
            return(Simpy(result)) 
