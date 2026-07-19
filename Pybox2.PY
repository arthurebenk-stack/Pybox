import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

background = pygame.image.load("let's add sprite/ronaldo.jpg")
background = pygame.transform.scale(background, (520, 420))

WHITE = (255, 255, 255)
BLUE = (0, 102, 204)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Rectangle🚶‍➡️📦")

clock = pygame.time.Clock()

rect_width = 100
rect_height = 60
rect_x = (SCREEN_WIDTH - rect_width) // 2
rect_y = (SCREEN_HEIGHT - rect_height) // 2
rect_speed = 5

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    if rect_x < 0:
        rect_x = 0
    if rect_x > SCREEN_WIDTH - rect_width:
        rect_x = SCREEN_WIDTH - rect_width
    if rect_y < 0:
        rect_y = 0
    if rect_y > SCREEN_HEIGHT - rect_height:
        rect_y = SCREEN_HEIGHT - rect_height

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

    clock.tick(FPS)