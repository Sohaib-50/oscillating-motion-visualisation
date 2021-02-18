import pygame

WIDTH = 700
HEIGHT = 700
BLACK = (0, 0, 0)
PURPLE = (77, 44, 82)
# RANDOM_COLOR = (35, 22, 155)
RANDOM_COLOR = (245, 237, 22)

window = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

i = 1
angle = 0
angular_velocity = 0.1241247800712847126498
while run:
    print(pygame.mouse.get_pos())
    # angular_velocity = ((WIDTH // 2) - pygame.mouse.get_pos()[0]) / 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angular_velocity -= 0.3
            if event.key == pygame.K_LEFT:
                angular_velocity += 0.3
            
    angle =  (angle + angular_velocity) % 360

    window.fill(PURPLE)
    rectangle_surface = pygame.Surface((500, 100))
    rectangle_surface.set_colorkey(BLACK)
    rectangle_surface.fill(RANDOM_COLOR)
    rectangle_surface = pygame.transform.rotate(rectangle_surface, angle)
    rectangle = rectangle_surface.get_rect()
    # pygame.Surface()
    # rectangle.rota
    rectangle.centerx = (pygame.mouse.get_pos()[0] - (WIDTH // 2)) + (WIDTH // 2)
    rectangle.centery = (pygame.mouse.get_pos()[1] - (HEIGHT // 2)) + (HEIGHT // 2)
    window.blit(rectangle_surface, rectangle)
    # pygame.draw.rect(window, RANDOM_COLOR, rectangle)
    pygame.display.update()
    i += 0.3

pygame.quit()




# import pygame as py  

# # define constants  
# WIDTH = 500  
# HEIGHT = 500  
# FPS = 30  

# # define colors  
# BLACK = (0 , 0 , 0)  
# GREEN = (0 , 255 , 0)  

# # initialize pygame and create screen  
# py.init()  
# screen = py.display.set_mode((WIDTH , HEIGHT))  
# # for setting FPS  
# clock = py.time.Clock()  

# rot = 0  
# rot_speed = 2  

# # define a surface (RECTANGLE)  
# image_orig = py.Surface((100 , 100))  
# # for making transparent background while rotating an image  
# image_orig.set_colorkey(BLACK)  
# # fill the rectangle / surface with green color  
# image_orig.fill(GREEN)  
# # creating a copy of orignal image for smooth rotation  
# image = image_orig.copy()  
# image.set_colorkey(BLACK)  
# # define rect for placing the rectangle at the desired position  
# rect = image.get_rect()  
# rect.center = (WIDTH // 2 , HEIGHT // 2)  
# # keep rotating the rectangle until running is set to False  
# running = True  
# while running:  
#     # set FPS  
#     clock.tick(FPS)  
#     # clear the screen every time before drawing new objects  
#     screen.fill(BLACK)  
#     # check for the exit  
#     for event in py.event.get():  
#         if event.type == py.QUIT:  
#             running = False  

#     # making a copy of the old center of the rectangle  
#     old_center = rect.center  
#     # defining angle of the rotation  
#     rot = (rot + rot_speed) % 360  
#     # rotating the orignal image  
#     new_image = py.transform.rotate(image_orig , rot)  
#     rect = new_image.get_rect()  
#     # set the rotated rectangle to the old center  
#     rect.center = old_center  
#     # drawing the rotated rectangle to the screen  
#     screen.blit(new_image , rect)  
#     # flipping the display after drawing everything  
#     py.display.flip()  

# py.quit()  