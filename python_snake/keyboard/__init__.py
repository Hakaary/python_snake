from enum import Enum


class Key(str, Enum):
    UP = "w"
    DOWN = "s"
    LEFT = "a"
    RIGHT = "d"
    QUIT = "q"


from .user_input import UserInput  # noqa: E402

__all__ = ["UserInput"]
