#main
import pygame,sys

from grid import Grid
from blocks import * #imports all classes
pygame.init()
dark_blue = (44,44,127) 
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris") #UI Title

clock = pygame.time.Clock() #timer

game_grid = Grid() #initializes the grid
#blocks code
block = LBlock()
#Output tests
game_grid.print_grid()
while True: #game logic loop for exiting the UI
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(dark_blue) #makes background dark blue
    game_grid.draw(screen) #draws the UI grid
    block.draw(screen) #draws the block
    pygame.display.update()
    clock.tick(60)
