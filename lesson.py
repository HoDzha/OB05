import pygame
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")
image = pygame.image.load('png-transparent-python-logo-thumbnail.png')
image_rect = image.get_rect()
speed = 1




run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            image_rect.x = mouse_x
            image_rect.y = mouse_y

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         image_rect.x -= speed
#     if keys[pygame.K_RIGHT]:
#         image_rect.x += speed
#     if keys[pygame.K_UP]:
#         image_rect.y -= speed
#     if keys[pygame.K_DOWN]:
#         image_rect.y += speed`


    screen.fill((0,100,0))
    screen.blit(image, image_rect)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
