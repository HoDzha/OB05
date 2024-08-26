import pygame

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
        self.body = []
        self.x_change = 0
        self.y_change = 0
        self.add_block()

    def add_block(self):
        self.body.append(Block(self.body[-1].x + block_size, self.body[-1].y))

    def draw(self):
        for block in self.body:
            block.draw()

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
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


# Создаем объекты
snake = Snake()
food = Block(200, 200)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.x_change = -block_size
                snake.y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake.x_change = block_size
                snake.y_change = 0
            elif event.key == pygame.K_UP:
                snake.y_change = -block_size
                snake.x_change = 0
            elif event.key == pygame.K_DOWN:
                snake.y_change = block_size
                snake.x_change = 0

    # Движение змейки
    snake.move()

    # Отрисовка
    screen.fill(black)
    snake.draw()
    food.draw()

    # Проверка столкновений
    # ... (добавьте проверку столкновений со стенками и самой змеей)
    check_collisions()
    pygame.display.update()