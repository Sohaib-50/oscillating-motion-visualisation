import pygame
from math import sin, cos, radians
from random import randint

WIDTH = 700
HEIGHT = 700
BLACK = (0, 0, 0)
PURPLE = (77, 44, 82)
RANDOM_COLOR = (245, 237, 22)

window = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

angle = 90
angular_velocity = -0.001
angular_acceleration = 0
LIMIT = randint(-2360, -2000)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if angle < LIMIT:
        angular_acceleration = 0.0035
    else:
        angular_acceleration = -0.0035

    if angular_velocity < 0:
        angular_velocity += angular_acceleration
    else:
        angular_velocity = 0
    angle = (angle + angular_velocity)
    print(round(angular_acceleration, 4), round(angular_velocity, 2), angle)

    window.fill(PURPLE)
    rectangle_surface = pygame.Surface((500, 4))
    rectangle_surface.set_colorkey(BLACK)
    rectangle_surface.fill(RANDOM_COLOR)
    rectangle_surface = pygame.transform.rotate(rectangle_surface, angle)
    rectangle = rectangle_surface.get_rect()
    rectangle.centerx = WIDTH // 2
    rectangle.centery = HEIGHT // 2
    pygame.draw.circle(window, (29, 46, 80), (WIDTH//2, HEIGHT//2), 280)
    pygame.draw.circle(window, (0, 0, 0),(WIDTH//2, HEIGHT//2), 250)
    pygame.draw.circle(window, (44, 44, 44),(WIDTH//2, HEIGHT//2), 25)
    window.blit(rectangle_surface, rectangle)
    pygame.draw.circle(window, (255, 255, 255),(WIDTH//2 + (250 * cos(radians(-angle))), HEIGHT//2 + (250 * sin(radians(-angle)))), 6)
    pygame.display.update()
    

pygame.quit()