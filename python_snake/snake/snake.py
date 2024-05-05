from typing import Self, List, Tuple, Set

from python_snake.snake import SnakeDirection


class SnakeNode:

    def __init__(
        self,
        direction: SnakeDirection,
        pos_x: int = 12,
        pos_y: int = 6,
        next_node: Self | None = None,
    ):
        self.direction = direction
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.next_node = next_node


class Snake:

    def __init__(
        self,
        head: SnakeNode,
        board_dimension: int,
        length: int = 1,
    ) -> None:
        self.head = head
        self.board_dimension = board_dimension
        self.length = length
        self.l_positions: List[Tuple[int, int]] = []
        self.s_positions: Set[Tuple[int, int]] = set()

        while head is not None:
            self.l_positions.append((head.pos_x, head.pos_y))
            self.s_positions.add((head.pos_x, head.pos_y))
            head = head.next_node  # type: ignore

    def change_head_direction(self, direction: SnakeDirection) -> None:
        if direction == SnakeDirection.UP and self.head.direction != SnakeDirection.DOWN:
            self.head.direction = direction
        if direction == SnakeDirection.DOWN and self.head.direction != SnakeDirection.UP:
            self.head.direction = direction
        if direction == SnakeDirection.LEFT and self.head.direction != SnakeDirection.RIGHT:
            self.head.direction = direction
        if direction == SnakeDirection.RIGHT and self.head.direction != SnakeDirection.LEFT:
            self.head.direction = direction

    def _move_up(self) -> None:
        self.head.pos_y -= 1
        if self.head.pos_y < 0:
            self.head.pos_y = self.board_dimension - 1

    def _move_down(self) -> None:
        self.head.pos_y += 1
        if self.head.pos_y >= self.board_dimension:
            self.head.pos_y = 0

    def _move_left(self) -> None:
        self.head.pos_x -= 1
        if self.head.pos_x < 0:
            self.head.pos_x = self.board_dimension - 1

    def _move_right(self) -> None:
        self.head.pos_x += 1
        if self.head.pos_x >= self.board_dimension:
            self.head.pos_x = 0

    def move(self) -> Tuple[int, int]:

        self.l_positions.clear()
        self.s_positions.clear()

        prev_node_position = (self.head.pos_x, self.head.pos_y)
        prev_node_direction = self.head.direction

        if self.head.direction == SnakeDirection.UP:
            self._move_up()
        if self.head.direction == SnakeDirection.DOWN:
            self._move_down()
        if self.head.direction == SnakeDirection.LEFT:
            self._move_left()
        if self.head.direction == SnakeDirection.RIGHT:
            self._move_right()

        self.l_positions.append((self.head.pos_x, self.head.pos_y))
        self.s_positions.add((self.head.pos_x, self.head.pos_y))

        current_node = self.head.next_node
        while current_node is not None:
            (
                current_node.pos_x,
                current_node.pos_y,
                prev_node_position,
                current_node.direction,
                prev_node_direction,
            ) = (
                prev_node_position[0],
                prev_node_position[1],
                (
                    current_node.pos_x,
                    current_node.pos_y,
                ),
                prev_node_direction,
                current_node.direction,
            )
            self.l_positions.append((current_node.pos_x, current_node.pos_y))
            self.s_positions.add((current_node.pos_x, current_node.pos_y))
            # prev_node_direction = current_node.direction
            current_node = current_node.next_node

        return prev_node_position

    def extend_snake(self) -> None:
        _tail = self.head

        # Get the tail of the snake
        while _tail.next_node is not None:
            _tail = _tail.next_node

        if _tail.direction == SnakeDirection.UP:
            new_node = SnakeNode(SnakeDirection.UP, _tail.pos_x, _tail.pos_y + 1)
        if _tail.direction == SnakeDirection.DOWN:
            new_node = SnakeNode(SnakeDirection.DOWN, _tail.pos_x, _tail.pos_y - 1)
        if _tail.direction == SnakeDirection.LEFT:
            new_node = SnakeNode(SnakeDirection.LEFT, _tail.pos_x + 1, _tail.pos_y)
        if _tail.direction == SnakeDirection.RIGHT:
            new_node = SnakeNode(SnakeDirection.RIGHT, _tail.pos_x - 1, _tail.pos_y)
        _tail.next_node = new_node
        self.l_positions.append((new_node.pos_x, new_node.pos_y))
        self.s_positions.add((new_node.pos_x, new_node.pos_y))

    def add_node(self, position: Tuple[int, int]) -> None:
        _tail = self.head

        # Get the tail of the snake
        while _tail.next_node is not None:
            _tail = _tail.next_node

        new_node = SnakeNode(SnakeDirection.UP, position[0], position[1])
        _tail.next_node = new_node
        self.l_positions.append((new_node.pos_x, new_node.pos_y))
        self.s_positions.add((new_node.pos_x, new_node.pos_y))

    def check_fruit(self, fruit_position: Tuple[int, int]) -> bool:
        return (self.head.pos_x, self.head.pos_y) == fruit_position

    def сheck_collision(self) -> bool:
        return len(self.l_positions) != len(self.s_positions)
