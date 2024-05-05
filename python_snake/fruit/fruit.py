from typing import Tuple, Set
from random import randint


class Fruit:

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
    ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

    def place_fruit(
        self, board_dimension: int, snake_positions: Set[Tuple[int, int]]
    ) -> Tuple[int, int]:
        x_rand = randint(0, board_dimension - 1)
        y_rand = randint(0, board_dimension - 1)

        while (x_rand, y_rand) in snake_positions:
            x_rand = randint(0, board_dimension - 1)
            y_rand = randint(0, board_dimension - 1)

        self.pos_x = x_rand
        self.pos_y = y_rand

        return self.pos_x, self.pos_y
