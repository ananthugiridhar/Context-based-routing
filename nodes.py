import pygame
import sys
from initializer import init_data
from graph_data import graph

# initializing the main function


def node():
    pygame.init()

    screen = pygame.display.set_mode(init_data['screen_dimension'])

    clock = pygame.time.Clock()

    screen.fill(init_data['background_color'])

    done = False

    pygame.draw.line(screen, init_data['screen_sep'][2], init_data['screen_sep']
                     [0], init_data['screen_sep'][1], width=init_data['screen_sep'][3])

    for coords, _ in graph:
        x = coords[0]
        y = coords[1]
        pygame.draw.circle(
            screen, init_data['node_init_color'][0], (x, y), init_data['node_radius'])
        pygame.draw.circle(
            screen, init_data['node_init_color'][1], (x, y), init_data['node_radius']-4)

    pygame.display.update()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()
