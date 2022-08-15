import keyboard
from time import sleep
import os
import datetime

class Snake():

    def __init__(self, posx=12, posy=6, next=None, char='#', direction=None):
        self.posx = posx
        self.posy = posy
        self.char = char
        self.next = next
        self.direction = direction 

class Snake_game():

    panel= [
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·']
            ]

    head_snake = Snake(char='@', next=Snake(posx=11, posy=6, next=Snake(posx=10, posy=6)), direction='right')

    def __init__(self):

        # Preparation
        os.system('cls' if os.name == 'nt' else 'clear')
        time = datetime.datetime.now()

        self.place_snake()
        self.print_game()

        while True:

            self.input_key()
            
            if (datetime.datetime.now() - time).microseconds >= 800000:

                # Calculate snakes new position
                last_tail_val = self.move_snake()
                # Reset panel
                self.clean_panel(last_tail_val)
                # Place snake in the panel
                self.place_snake()

                # Final step
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_game()

                # Refresh time
                time = datetime.datetime.now()

    def input_key(self):

        if keyboard.is_pressed('d') and self.head_snake.direction is not 'left':
            self.head_snake.direction = 'right'
        elif keyboard.is_pressed('a') and self.head_snake.direction is not 'right':
            self.head_snake.direction = 'left'
        elif keyboard.is_pressed('w') and self.head_snake.direction is not 'down':
            self.head_snake.direction = 'up'
        elif keyboard.is_pressed('s') and self.head_snake.direction is not 'up':
            self.head_snake.direction = 'down'

    def move_snake(self):
       
        snake = self.head_snake       

        # Move head
        prev_position = (snake.posx, snake.posy)

        if snake.direction == 'right':
            if snake.posx + 1 < len(self.panel[snake.posy]):
                snake.posx = snake.posx + 1
            else:
                snake.posx = 0
        elif snake.direction == 'left':
            if snake.posx - 1 >= 0:
                snake.posx = snake.posx - 1
            else:
                snake.posx = len(self.panel[snake.posy]) - 1
        elif snake.direction == 'up':
            if snake.posy - 1 >= 0:
                snake.posy = snake.posy - 1
            else:
                snake.posy = len(self.panel) - 1
        elif snake.direction == 'down':
            if snake.posy + 1 < len(self.panel):
                snake.posy = snake.posy + 1
            else:
                snake.posy = 0

        # Move tail
        snake = snake.next

        while snake is not None:
            prev_position, snake.posx, snake.posy = (snake.posx, snake.posy), prev_position[0], prev_position[1]
            snake = snake.next

        return (prev_position)

    def clean_panel(self, last_tail_val):

        self.panel[last_tail_val[1]][last_tail_val[0]] = '·'

    def place_snake(self):

        snake = self.head_snake
        snake_placement = []

        while snake is not None:
            snake_placement.append((snake.posx, snake.posy, snake.char))
            snake = snake.next

        for pos in snake_placement:
            self.panel[pos[1]][pos[0]] = pos[2]

    def print_game(self):

        for i in range(len(self.panel)):
            for j in range(len(self.panel[i])):
                print(self.panel[i][j], end='')
            print()


if __name__ == "__main__":
    
    game = Snake_game()

