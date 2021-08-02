import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600
serface = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont('roboto', 35)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()