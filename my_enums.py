from enum import Enum
class Keys(Enum):
    ball = "ball"
    cell = "cell"
    row = "row"
    column = "column"

class Ball(Enum):
    purpule = "P"
    red = "R"
    grey = "G"
    none = "N"

class Cell(Enum):
    target = "o"
    path  = "."
