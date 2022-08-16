import keyboard
from time import sleep
import os
import datetime
import random

class Snake():

    def __init__(self, posx=12, posy=6, next=None, char='#', direction=None, positions=None,length=None):
        self.posx = posx
        self.posy = posy
        self.char = char
        self.next = next
        self.direction = direction
        self.positions = positions
        self.length = length

class Fruit():

    def __init__(self, posx=None, posy=None, placed=False):
        self.posx = posx
        self.posy = posy
        self.placed = placed

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
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
            ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ]

    head_snake = Snake(char='@', next=Snake(posx=11, posy=6, next=Snake(posx=10, posy=6)), direction='right', positions={(12, 6), (11, 6), (10, 6)}, length=3)
    prev_direction = head_snake.direction
    fruit = Fruit()

    def __init__(self):

        # Preparation
        os.system('cls' if os.name == 'nt' else 'clear')
        time = datetime.datetime.now()

        self.place_snake()
        self.print_game()

        sleep(1)

        # Place fruit
        self.place_fruit()

        while True:

            self.input_key()
            
            if (datetime.datetime.now() - time).microseconds >= 800000:

                # Calculate snakes new position
                last_tail_val = self.move_snake()

                # Check if the snake has gone over itself
                self.check_end()

                # Reset panel
                self.clean_panel(last_tail_val)

                # Check if new position includes fruit
                if self.is_fruit():            
                    self.append_tail(last_tail_val)

                # Place snake in the panel
                self.place_snake()

                # Place fruit
                self.place_fruit()

                # Final step 
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_game()

                print(self.head_snake.positions)
                print(len(self.head_snake.positions))
                print(self.head_snake.length)

                # Refresh time and prev_direction
                time = datetime.datetime.now()
                self.prev_direction = self.head_snake.direction

    def input_key(self):

        # Prevents being able to turn over the snake itself
        if self.prev_direction is not self.head_snake.direction:
            return

        if keyboard.is_pressed('d') and self.head_snake.direction is not 'left':
            self.head_snake.direction = 'right'
        elif keyboard.is_pressed('a') and self.head_snake.direction is not 'right':
            self.head_snake.direction = 'left'
        elif keyboard.is_pressed('w') and self.head_snake.direction is not 'down':
            self.head_snake.direction = 'up'
        elif keyboard.is_pressed('s') and self.head_snake.direction is not 'up':
            self.head_snake.direction = 'down'

    def check_end(self):

        if self.head_snake.length == (len(self.panel[0]) * len(self.panel)):
            os.system('cls' if os.name == 'nt' else 'clear')

            print("#   #   #   # #  #   #")
            print(" #   # #   #  #  ##  #")
            print("  #   #   #   #  # # #")
            print("   # # # #    #  #  ##")
            print("    #   #     #  #   #")

            exit()

        if self.head_snake.length != len(self.head_snake.positions):
            os.system('cls' if os.name == 'nt' else 'clear')

            print("#####     #      #  #")
            print("#        # #     #  #")
            print("###     #####    #  #")
            print("#      #     #   #  #")
            print("#     #       #  #  #####")

            exit()

    def append_tail(self, last_tail_val):

        snake = self.head_snake

        while snake.next is not None:
            snake = snake.next

        snake.next = Snake(posx=last_tail_val[0], posy=last_tail_val[1])

        self.head_snake.length = self.head_snake.length + 1

    def is_fruit(self):

        if self.head_snake.posx == self.fruit.posx and self.head_snake.posy == self.fruit.posy:
            
            self.fruit.placed = False

            return True

        return False

    def place_fruit(self):

        if not self.fruit.placed:

            possible_positions = set([(a, b) for b in range(len(self.panel)) for a in range(len(self.panel[0]))]) - self.head_snake.positions
            possible_positions = list(possible_positions) 
            position = random.choice(possible_positions)

            self.panel[position[1]][position[0]] = '+'

            self.fruit.posx = position[0]
            self.fruit.posy = position[1]

            self.fruit.placed = True

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
            self.panel[snake.posy][snake.posx] = snake.char
            snake_placement.append((snake.posx, snake.posy))
            snake = snake.next

        self.head_snake.positions = set(snake_placement)

    def print_game(self):

        for i in range(len(self.panel)):
            for j in range(len(self.panel[i])):
                print(self.panel[i][j], end=' ')
            print()


if __name__ == "__main__":
    
    game = Snake_game()

