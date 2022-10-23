import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
SPEED = 40

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)


class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display window
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake Game AI")
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT

        # init snake
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-BLOCK_SIZE, self.head.y), Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None

        # init the food
        self._place_food()

    # place the food in a random position on the display window
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE

        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        # 1. Get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                if event.key == pygame.K_UP:
                    self.direction = Direction.UP

        # 2. Move the snake
        self.move(self.direction)
        self.snake.insert(0, self.head)

        # 3. Check if the game is over
        game_over = False
        if self._is_collision(self):
            game_over = True
            return game_over, score
        # 4. Place the new food

        # 5. Update the ui and the clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. Return if game over and the score
        return game_over, self.score

    def _is_collision(self):
        # Check if the snake hits the boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h-BLOCK_SIZE or self.head.y < 0:
            return True

        # Check if the snake hits itself
        if self.head in self.snake[1:]:
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
    
    def move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == direction.DOWN:
            y += BLOCK_SIZE
        elif direction == direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

if __name__ == '__main__':
    game = SnakeGame()

    # The main game loop
    while True:
        game_over, score = game.play_step()

        # Break the game loop if it is over
        if game_over == True:
            break

    print("Final Score", score)

    pygame.quit()