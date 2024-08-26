import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLOCK_SIZE = 20
SNAKE_SPEED = 11

# Настройка экрана
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Snake Game')

# Часы для контроля FPS
clock = pygame.time.Clock()

# Шрифты для текста
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((DISPLAY_WIDTH // 2), (DISPLAY_HEIGHT // 2))]
        # Начальное направление движения змейки, как кортеж (0, -1) движется вверх
        self.direction = (0, -1)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        # Проверка на попытку развернуться в противоположном направлении
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * BLOCK_SIZE)) % DISPLAY_WIDTH), (cur[1] + (y * BLOCK_SIZE)) % DISPLAY_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((DISPLAY_WIDTH // 2), (DISPLAY_HEIGHT // 2))]
        self.direction = (0, -1)
        self.score = 0

    def grow(self):
        self.length += 1
        self.score += 1

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, GREEN, pygame.Rect(p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (DISPLAY_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (DISPLAY_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game_loop():
    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.turn((1, 0))

        snake.move()

        # Проверка столкновения с едой
        if snake.get_head_position() == food.position:
            snake.grow()
            food.randomize_position()

        display.fill(BLUE)
        snake.draw(display)
        food.draw(display)

        # Отображение счета
        draw_text("Score: {}".format(snake.score), score_font, WHITE, display, 10, 10)

        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
# Завершение Pygame

