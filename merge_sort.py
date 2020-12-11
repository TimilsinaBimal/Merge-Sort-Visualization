import pygame
import random

HEIGHT = 600
WIDTH = 800

# Screen Colors
WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (0, 56, 147)
GREEN = (46, 204, 114)
PURPLE = (187, 44, 217)


def generate_array(start, end, num):
    arr = [random.randint(start, end+1) for _ in range(num)]
    return arr


arr = generate_array(10, 50, 100)
arr_color = [GREEN for _ in range(len(arr))]


def prepare_screen():
    """
    Create the initial screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("MERGE SORT VISUALIZATION")
    return screen


screen = prepare_screen()


def refill():
    screen.fill(WHITE)
    draw()
    pygame.display.update()
    pygame.time.delay(100)


def draw():
    pos = 10
    for idx, i in enumerate(arr):
        left = pos + 8
        pygame.draw.rect(screen, arr_color[idx], (left, 0, 6, i*10))
        pos = left


def sort(arr, l, r):
    mid_index = (l+r)//2
    if l < r:
        sort(arr, l, mid_index)
        sort(arr, mid_index+1, r)
        merge(arr, l, mid_index, mid_index+1, r)


def merge(arr, l_start, l_end, r_start, r_end):
    i = l_start
    j = r_start
    temp = []
    pygame.event.pump()
    while i <= l_end and j <= r_end:
        arr_color[i] = RED
        arr_color[j] = RED
        refill()
        arr_color[i] = GREEN
        arr_color[j] = GREEN
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= l_end:
        arr_color[i] = RED
        refill()
        arr_color[i] = GREEN
        temp.append(arr[i])
        i += 1

    while j <= r_end:
        arr_color[j] = RED
        refill()
        arr_color[j] = GREEN
        temp.append(arr[j])
        j += 1

    k = 0
    for i in range(l_start, r_end+1):
        pygame.event.pump()
        arr[i] = temp[k]
        k += 1
        arr_color[i] = BLUE
        refill()
        if r_end-l_start == len(arr) - 1:
            arr_color[i] = PURPLE
        else:
            arr_color[i] = GREEN


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            sort(arr, 0, len(arr)-1)
            draw()
            pygame.quit()
            quit()
    # draw()
    # pygame.display.update()
    # pygame.quit()
    quit()
