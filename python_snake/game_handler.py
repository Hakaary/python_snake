import logging.handlers
import os
from datetime import datetime, timedelta
from threading import Thread
import logging

from python_snake.keyboard import UserInput, Key
from python_snake.board import Board
from python_snake.snake import Snake, SnakeNode, SnakeDirection
from python_snake.fruit import Fruit

BOARD_DIMENSION = 15
TICK_RATE = 3
LOG_LEVEL = logging.CRITICAL


class GameHandler:

    def __init__(self) -> None:
        self.board: Board | None = None
        self.snake: Snake | None = None
        self.fruit: Fruit | None = None
        self.user_input: UserInput | None = None

        self.tick_rate = float(TICK_RATE)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(LOG_LEVEL)
        def_logger = logging.StreamHandler()
        def_logger.setLevel(LOG_LEVEL)
        formatter = logging.Formatter("%(levelname)s - %(message)s")
        def_logger.setFormatter(formatter)
        self.logger.addHandler(def_logger)

    def __init_board(self, dimension: int) -> None:
        self.board = Board(dimension)

    def __init_snake(
        self, initial_direction: SnakeDirection, initial_length: int = 2
    ) -> None:
        self.snake = Snake(
            SnakeNode(
                initial_direction,
                BOARD_DIMENSION // 2,
                BOARD_DIMENSION // 2,
            ),
            BOARD_DIMENSION,
        )
        for _ in range(initial_length):
            self.snake.extend_snake()

    def __init_fruit(self) -> None:
        self.fruit = Fruit(0, 0)
        self.fruit.place_fruit(
            BOARD_DIMENSION,
            self.snake.s_positions,  # type: ignore
        )

    def __init_keyboard_capture(self) -> None:
        self.user_input = UserInput()
        thread = Thread(target=self.user_input.start_retrieving_input)
        thread.daemon = True
        thread.start()

    def run(self) -> None:
        print("Running game...")

        # Inits
        self.__init_board(BOARD_DIMENSION)
        self.__init_snake(SnakeDirection.RIGHT)
        self.__init_fruit()
        self.__init_keyboard_capture()

        # Check vars are initialized
        if self.board is None:
            raise ValueError("Board not initialized")
        if self.snake is None:
            raise ValueError("Snake not initialized")
        if self.fruit is None:
            raise ValueError("Fruit not initialized")
        if self.user_input is None:
            raise ValueError("User input not initialized")

        lst_frame = datetime.now()

        os.system("cls" if os.name == "nt" else "clear")

        while True:

            # Quit game
            if self.user_input.last_key == Key.QUIT:
                os.system("cls" if os.name == "nt" else "clear")
                break

            # Frame rate control
            if (
                lst_frame + timedelta(seconds=(1 / self.tick_rate))
                > datetime.now()
            ):
                continue
            lst_frame = datetime.now()

            if self.user_input.last_key == Key.UP:
                self.snake.change_head_direction(
                    SnakeDirection(SnakeDirection.UP)
                )
            if self.user_input.last_key == Key.DOWN:
                self.snake.change_head_direction(
                    SnakeDirection(SnakeDirection.DOWN)
                )
            if self.user_input.last_key == Key.LEFT:
                self.snake.change_head_direction(
                    SnakeDirection(SnakeDirection.LEFT)
                )
            if self.user_input.last_key == Key.RIGHT:
                self.snake.change_head_direction(
                    SnakeDirection(SnakeDirection.RIGHT)
                )

            # Move
            tail_last_pos = self.snake.move()
            # Check if snake eats fruit
            if self.snake.check_fruit((self.fruit.pos_x, self.fruit.pos_y)):
                self.snake.add_node(tail_last_pos)
                # Check if snake won
                if len(self.snake.s_positions) == BOARD_DIMENSION**2:
                    exit("You won!")
                self.fruit.place_fruit(BOARD_DIMENSION, self.snake.s_positions)

            # Check if snake collides with itself
            if self.snake.сheck_collision():
                os.system("cls" if os.name == "nt" else "clear")
                exit("Game over!")

            self.board.clean_board(tail_last_pos)

            # Draw snake, fruit and board
            self.board.place_fruit((self.fruit.pos_x, self.fruit.pos_y))
            self.board.place_snake(self.snake.l_positions)
            self.board.draw_board()

            self.logger.debug(f"Snake positions: {self.snake.l_positions}")
            self.logger.debug(f"Last key pressed: {self.user_input.last_key}")
