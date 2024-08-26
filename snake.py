import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Размер блока
block_size = 10
clock = pygame.time.Clock()  # Для управления скоростью игры

# Класс для блоков
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, green, [self.x, self.y, block_size, block_size])

# Класс для змейки
class Snake:
    def __init__(self):
        self.body = [Block(width // 2, height // 2)]  # Начальная позиция змейки
        self.x_change = 0
        self.y_change = 0

    def add_block(self):
        last_block = self.body[-1]
        self.body.append(Block(last_block.x, last_block.y))

    def draw(self):
        for block in self.body:
            block.draw()

    def move(self):
        # Перемещаем тело змейки
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        # Перемещаем голову
        self.body[0].x += self.x_change
        self.body[0].y += self.y_change

def check_collisions():
    # Столкновение со стенками
    if snake.body[0].x < 0 or snake.body[0].x >= width or snake.body[0].y < 0 or snake.body[0].y >= height:
        return True
    # Столкновение с самой собой
    for block in snake.body[1:]:
        if snake.body[0].x == block.x and snake.body[0].y == block.y:
            return True
    return False

def spawn_food():
    return Block(random.randint(0, (width - block_size) // block_size) * block_size,
                 random.randint(0, (height - block_size) // block_size) * block_size)

# Создаем объекты
snake = Snake()
food = spawn_food()

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.x_change == 0:
                snake.x_change = -block_size
                snake.y_change = 0
            elif event.key == pygame.K_RIGHT and snake.x_change == 0:
                snake.x_change = block_size
                snake.y_change = 0
            elif event.key == pygame.K_UP and snake.y_change == 0:
                snake.y_change = -block_size
                snake.x_change = 0
            elif event.key == pygame.K_DOWN and snake.y_change == 0:
                snake.y_change = block_size
                snake.x_change = 0

    # Движение змейки
    snake.move()

    # Проверка столкновений
    if check_collisions():
        running = False

    # Проверка на съедание еды
    if snake.body[0].x == food.x and snake.body[0].y == food.y:
        snake.add_block()
        food = spawn_food()

    # Отрисовка
    screen.fill(black)
    snake.draw()
    food.draw()
    pygame.display.update()

    clock.tick(10)  # Ограничение скорости до 10 FPS (можете изменить значение для ускорения или замедления)

# Завершение Pygame
pygame.quit()
