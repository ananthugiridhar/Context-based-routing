import pygame
from graph_data import graph
from initializer import init_data


def deploy_network():

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
    clock.tick(5)
    pygame.time.delay(3000)

    for coords, _ in graph:
        draw_circles(coords)

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


def draw_circles(coords):

    pygame.draw.circle(
        screen, init_data['node_init_color'][0], coords, init_data['node_radius'])
    if coords == (350, 490):
        pygame.draw.circle(
            screen, init_data['red'], coords, init_data['node_radius']-4)
    elif coords == (140, 420):
        pygame.draw.circle(
            screen, init_data['red'], coords, init_data['node_radius']-4)
    else:
        pygame.draw.circle(
            screen, init_data['node_init_color'][1], coords, init_data['node_radius']-4)


def screenSep():
    pygame.draw.line(screen, init_data['screen_sep'][2], init_data['screen_sep']
                     [0], init_data['screen_sep'][1], width=init_data['screen_sep'][3])
