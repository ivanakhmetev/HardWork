#
from tkinter import SW
import pygame
from glovals import SHEIGHT, SWIDTH, WHITE, BLUE


def start():
    
    pygame.init()
    screen = pygame.display.set_mode([SWIDTH, SHEIGHT])
    
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(WHITE)
        pygame.display.flip()

    pygame.quit()
    
start()