import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

# Changes from Snake Game ------------

# 1. Agent should reset the game after each game_over
# 2. Reward function
# 3. Change the play() function to compute and return the direction to take
# 4. Keep track of the current game iteration
# 5. Make changes to the is_collision function


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
SPEED = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)


class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display window
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake Game AI")
        self.clock = pygame.time.Clock()
        self.reset()


    def reset(self):
        # init game state
        self.direction = Direction.RIGHT

        # init snake
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-BLOCK_SIZE, self.head.y), Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None

        # init the food
        self._place_food()
        
        self.frame_iteration = 0

    # place the food in a random position on the display window
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE

        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        # 1. Move the snake based on generated action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. Move the snake
        self.move(action)
        self.snake.insert(0, self.head)

        # 3. Check if the game is over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, score

        # 4. Place the new food
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        # 5. Update the ui and the clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. Return if game over and the score
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # Check if the snake hits the boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h-BLOCK_SIZE or pt.y < 0:
            return True

        # Check if the snake hits itself
        if pt in self.snake[1:]:
            return True

        return False


    def _update_ui(self):
        self.display.fill(BLACK)

        # Drawing the snake
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        # Drawing the food
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        # Drawing the score
        text = font.render("Score: " + str(self.score), True, WHITE)

        self.display.blit(text, [0, 0])
        pygame.display.flip()
    
    def move(self, action):
        # [straight, right, left]
        # Define all possible directions in a clockwise order
        clockwise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clockwise.index(self.direction)

        if(np.array_equals(action, [1,0,0])):
            new_direction = clockwise[idx] # no change to the direction
        elif(np.array_equals(action, [0,1,0])):
            next_index = (idx + 1) % 4 # make a right turn
            new_dir = clock_wise[next_index]
        else:
            next_index = (idx - 1) % 4 # make a left turn
            new_dir = clock_wise[next_index]

        self.direction = new_dir

        x = self.head.x
        y = self.head.y

        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

# if __name__ == '__main__':
#     game = SnakeGame()

#     # The main game loop
#     while True:
#         game_over, score = game.play_step()

#         # Break the game loop if it is over
#         if game_over == True:
#             break

#     print("Final Score", score)

#     pygame.quit()