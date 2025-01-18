import pygame,sys

#initialing the pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GREEN = (20, 160, 133)

#ball parameters
ball_x = 400
ball_y = 400

ball_radius = 20

ball_speed_x = 0
ball_speed_y = 0

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("my first pygame game")

clock = pygame.time.Clock()

#game loop
while True:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_speed_x = 3
            elif event.key == pygame.K_LEFT:
                ball_speed_x = -3
            elif event.key == pygame.K_UP:
                ball_speed_y = -3
            elif event.key == pygame.K_DOWN:
                ball_speed_y = 3
            
    #updating the positions
    
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    #Drawing
    window.fill(GREEN)
    pygame.draw.circle(window, pygame.Color('white') ,(ball_x, ball_y), ball_radius)
    
    pygame.display.update()
    clock.tick(60)

