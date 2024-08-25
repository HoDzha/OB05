import pygame
pygame.inint()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.caption = "Тестовый проект"
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()