#1

# import pygame
# pygame.init()
# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)
# pygame.display.set_caption("Игра Даши")
# screen = pygame.display.set_mode((800, 600))

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.update()

# pygame.quit()

#2

# import pygame
# import random
# pygame.init()

# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)
# pygame.display.set_caption("Игра Даши")
# screen_width = 800
# screen_height= 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# BLACK = (0, 0, 0)      
# WHITE = (255, 255, 255) 
# RED = (255, 0, 0)       
# GREEN = (0, 255, 0)    

# snake_block_size = 10 
# snake_speed = 50
# clock = pygame.time.Clock()
# snake_x = screen_width / 2
# snake_y = screen_height / 2
# snake_x_change = 0
# snake_y_change = 0
# food_x = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
# food_y = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0
# game_over = False

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT: 
#                 snake_x_change = -snake_block_size
#                 snake_y_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 snake_x_change = snake_block_size
#                 snake_y_change = 0
#             elif event.key == pygame.K_UP:
#                 snake_y_change = -snake_block_size
#                 snake_x_change = 0
#             elif event.key == pygame.K_DOWN: 
#                 snake_y_change = snake_block_size
#                 snake_x_change = 0

#     snake_x += snake_x_change
#     snake_y += snake_y_change
#     screen.fill(WHITE)
#     pygame.draw.rect(screen, RED, [food_x, food_y, snake_block_size, snake_block_size])
#     pygame.draw.rect(screen, GREEN, [snake_x, snake_y, snake_block_size, snake_block_size])
#     pygame.display.update()

#     if snake_x == food_x and snake_y == food_y:
#         print("Ням!")
#         food_x = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
#         food_y = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0
#     clock.tick(snake_speed)

# pygame.quit()
# quit()

#3

import pygame
import random
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Прыгающий Кролик')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)  
BLUE = (0, 0, 255)  
clock = pygame.time.Clock()
fps = 60 
player_width = 30
player_height = 30
player_x = 50
player_y = screen_height - player_height - 10
ground_y = player_y 

player_y_velocity = 0
gravity = 0.8         
jump_strength = -15   
is_jumping = False   

obstacle_width = 20
obstacle_height = 40
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_height - 10 
obstacle_speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if not is_jumping:
                    player_y_velocity = jump_strength
                    is_jumping = True

    if is_jumping:
        player_y_velocity += gravity 
        player_y += player_y_velocity 

        if player_y >= ground_y:
            player_y = ground_y
            is_jumping = False
            player_y_velocity = 0

    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = screen_width + random.randint(50, 200)

    screen.fill(BLACK)
    player_rect = pygame.draw.rect(screen, BLUE, [player_x, player_y, player_width, player_height])
    obstacle_rect = pygame.draw.rect(screen, RED, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])

    if player_rect.colliderect(obstacle_rect):
        print("Столкновение!") 
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
quit()