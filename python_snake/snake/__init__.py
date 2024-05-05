from enum import Enum


class SnakeCharacter(str, Enum):

    HEAD = "@"
    BODY = "#"


class SnakeDirection(str, Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


from .snake import Snake, SnakeNode  # noqa: E402

__all__ = ["Snake", "SnakeNode", "SnakeDirection"]
