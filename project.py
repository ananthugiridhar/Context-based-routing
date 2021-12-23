
import pygame
import math
from graph_data import graph, Battery
import graph_data
from initializer import init_data

NoOfNodes = len(graph)
parent = [0 for i in range(NoOfNodes)]
visited = [False for i in range(NoOfNodes)]
value = [10000 for i in range(NoOfNodes)]
edge_color = {}
battery_status = ['color_white' for i in range(NoOfNodes)]


def project():

    global edges, screen, clock, speed, Heading_font, Battery_font, info_font, info_to_display, path_to_display
    speed = 5
    info_to_display = ""
    path_to_display = ''

    pygame.init()

    done = False

    screen = pygame.display.set_mode(init_data['screen_dimension'])
    Heading_font = pygame.font.Font('freesansbold.ttf', 20)
    Battery_font = pygame.font.SysFont('monospace', 15)
    info_font = pygame.font.SysFont('monospace', 17)

    clock = pygame.time.Clock()

    screenSep()

    build_edges()
    add_weights()
    graph_data.randomBattery()

    show_info()

    print(Battery)

    add_color()

    draw_network()
    info_to_display = "adding network"

    info_to_display = "finding initial optimal path"

    print("end")

    delay_time(2000)
    print(parent)
    info_to_display = "optimal path tree is formed"
    update_init_network()

    destination = 0
    while destination != -1:
        setZero()

        delay_time(2)
        source, destination, priority = input(
            'give the source and dest you want to reach  :  ').split()
        source = int(source)
        destination = int(destination)
        update_init_network()
        dijkstra(source, False)
        # dijkstra(source, False)
        delay_time(2)
        info_to_display = "finding optimal path from " + \
            str(source) + " to " + str(destination) + " ......"
        # update_init_network()
        find_path(destination)
        delay_time(2)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()


def dijkstra(source, status):
    start = source
    parent[start] = -1
    value[start] = 0
    for i in range(NoOfNodes):
        minNode = findMinNode()
        visited[minNode] = True

        for j in range(len(graph[minNode][1])):
            currNode = graph[minNode][1][j]
            weight = graph[minNode][2][j]
            if status == True:
                if visited[currNode] == False and value[minNode] < 10000 and (value[minNode] + weight < value[currNode]):
                    value[currNode] = value[minNode] + weight
                    parent[currNode] = minNode

            if visited[currNode] == False and value[minNode] < 10000 and (value[minNode] + weight < value[currNode]) and Battery[currNode] > 49:
                value[currNode] = value[minNode] + weight
                parent[currNode] = minNode


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


def draw_circles(coords, color):
    pygame.draw.circle(
        screen, init_data['node_init_color'][0], coords, init_data['node_radius'])
    pygame.draw.circle(
        screen, init_data[color], coords, init_data['node_radius']-4)


def screenSep():
    pygame.draw.rect(
        screen, init_data['screen_sep_color'], pygame.Rect(800, 10, 1190, 690))
    pygame.display.flip()
    pygame.draw.line(screen, init_data['screen_sep'][2], init_data['screen_sep']
                     [0], init_data['screen_sep'][1], width=init_data['screen_sep'][3])


def update_network():
    global clock, speed
    draw_network()
    show_info()
    pygame.display.flip()
    clock.tick(10)


def add_color():
    for i in edges:
        edge_color[i] = 'color_white'
    for i in range(NoOfNodes):
        graph[i].append('blue')


def update_init_color():
    for i in edges:
        edge_color[i] = 'color_white'
    for i in range(NoOfNodes):
        graph[i][3] = 'blue'


def update_init_network():
    update_init_color()
    update_network()


def draw_network():
    for start, end in edges:
        col = (start, end)
        line_col = edge_color[col]
        pygame.draw.line(
            screen, init_data[line_col], graph[start][0], graph[end][0], 3)

    for coords, _, _, color in graph:
        draw_circles(coords, color)

    delay_time(1)


def add_weights():

    for index, (start, connections) in enumerate(graph):
        weight = []
        x1 = start[0]
        y1 = start[1]
        for end in connections:
            x2 = graph[end][0][0]
            y2 = graph[end][0][1]

            dis = pow((x2 - x1), 2) + pow((y2 - y1), 2)
            dis = int(math.sqrt(dis))

            weight.append(dis)

        graph[index].append(weight)


def algo(start):
    parent[start] = -1
    value[start] = 0

    for i in range(NoOfNodes-1):
        minNode = findMinNode()
        visited[minNode] = True

        for j in range(len(graph[minNode][1])):
            currNode = graph[minNode][1][j]
            weight = graph[minNode][2][j]
            if visited[currNode] == False and value[minNode] < 10000 and (value[minNode] + weight < value[currNode]):
                value[currNode] = value[minNode] + weight
                parent[currNode] = minNode


def findMinNode():
    minimum = 1000000
    for i in range(NoOfNodes):
        if visited[i] == False and value[i] < minimum:
            node = i
            minimum = value[i]

    return node


def find_path(dest):
    route = []
    temp = dest
    global info_to_display, path_to_display

    while(temp != -1):
        route.append(temp)
        temp = parent[temp]

    route.reverse()
    print(route)

    for index, data in enumerate(route):
        Battery[data] = Battery[data] - 10
        if Battery[data] < 50:
            battery_status[data] = 'red'
        graph[data][3] = 'red'
        if index+1 < len(route):
            pos = (data, route[index+1])
            edge_color[pos] = 'red'
        delay_time(100)

        update_network()
    info_to_display = "optimal path found"
    pp = ""
    for i in route:
        if i < len(route):
            pp = pp + str(i) + " --> "

    path_to_display = pp

    # prev = temp
    # temp = parent[temp]
    # graph[temp][3] = 'red'
    # pos = (prev, temp)
    # edge_color[pos] = 'red'
    # graph[NoOfNodes-1][3] = 'blue'
    # update_network()
    # delay_time(100)

    # update_network()


def delay_time(delay):
    pygame.display.flip()
    pygame.time.wait(delay)


def show_info():
    Heading = Heading_font.render('INFO SECTION', True,
                                  init_data['color_white'], init_data['screen_sep_color'])
    screen.blit(Heading, (920, 50))

    info = info_font.render(info_to_display, True,
                            init_data['color_white'], init_data['screen_sep_color'])
    screen.blit(info, (850, 150))

    path = info_font.render(path_to_display, True,
                            init_data['color_white'], init_data['screen_sep_color'])
    screen.blit(path, (850, 600))

    for index, percentage in enumerate(Battery):
        txt = "Node " + str(index) + " : " + str(percentage)
        loc = (index * 15) + 200
        bat = Battery_font.render(
            txt, True, init_data[battery_status[index]], init_data['screen_sep_color'])
        screen.blit(bat, (900, loc))


def setZero():
    for i in range(NoOfNodes):
        parent[i] = 0
    for i in range(NoOfNodes):
        visited[i] = False
    for i in range(NoOfNodes):
        value[i] = 10000
