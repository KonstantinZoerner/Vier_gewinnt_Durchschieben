import pygame, sys

screen = pygame.display.set_mode((400, 400))
pygame.init()
clock = pygame.time.Clock()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            druck_pos = pygame.mouse.get_pos()


    pygame.display.flip()
