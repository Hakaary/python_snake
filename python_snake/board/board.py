from typing import List, Tuple

from python_snake.snake import SnakeCharacter


class Board:

    def __init__(self, dimension: int) -> None:
        self.board: List[List[str]] = [[]]

        for i in range(dimension):
            self.board.append([])
            for _ in range(dimension):
                self.board[i].append("·")

    def clean_whole_board(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = "·"

    def clean_board(self, tail_last_value: Tuple[int, int]) -> None:
        self.board[tail_last_value[1]][tail_last_value[0]] = "·"

    def place_snake(self, snake_positions: List[Tuple[int, int]]) -> None:
        for pos in reversed(snake_positions[1:]):
            self.board[pos[1]][pos[0]] = SnakeCharacter.BODY.value
        self.board[snake_positions[0][1]][snake_positions[0][0]] = SnakeCharacter.HEAD.value

    def place_fruit(self, fruit_position: Tuple[int, int]) -> None:
        self.board[fruit_position[1]][fruit_position[0]] = "$"

    def draw_board(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print()
