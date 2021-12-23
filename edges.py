import pygame
from graph_data import graph
from initializer import init_data


def run():

    global edges, screen

    pygame.init()
    done = False

    screen = pygame.display.set_mode(init_data['screen_dimension'])

    clock = pygame.time.Clock()

    screenSep()

    build_edges()

    for start, end in edges:
        pygame.draw.line(
            screen, init_data['color_white'], graph[start][0], graph[end][0], 2)

    pygame.display.update()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()


def edge_id(n1, n2):  # normalize id for either order
    # (1,2) and (2,1) become (1,2)
    return tuple(sorted((n1, n2)))


def build_edges():
    global edges
    edges = {}
    for n1, (_, adjacents) in enumerate(graph):
        for n2 in adjacents:
            eid = edge_id(n1, n2)
            if eid not in edges:
                edges[eid] = (n1, n2)


def screenSep():
    pygame.draw.line(screen, init_data['screen_sep'][2], init_data['screen_sep']
                     [0], init_data['screen_sep'][1], width=init_data['screen_sep'][3])
