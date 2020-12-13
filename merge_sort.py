import pygame
import random


def generate_array(start, end, num):
    arr = [random.randint(start, end+1) for _ in range(num)]
    return arr


def render_font(screen):
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, 100))
    bold_font = pygame.font.SysFont('sfprodisplaysemibold', 32)
    regular_font = pygame.font.SysFont('sfprodisplayregular', 20)
    title = bold_font.render('Merge Sort Visualization', True, WHITE)
    text2 = regular_font.render('Press ENTER to Start.', True, WHITE)
    text3 = regular_font.render('Press Q to quit.', True, WHITE)
    text4 = regular_font.render('Press G to generate new Array.', True, WHITE)
    textRect = title.get_rect()
    textRect.center = (WIDTH//2, 100 // 3)
    screen.blit(title, textRect)
    screen.blit(text2, (20, 60))
    screen.blit(text3, (WIDTH//3, 60))
    screen.blit(text4, (WIDTH-300, 60))
    pygame.draw.line(screen, BLACK, (0, 100), (WIDTH, 100), 9)


def prepare_screen():
    """
    Create the initial screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("MERGE SORT VISUALIZATION")
    return screen


def refill():
    screen.fill(WHITE)
    draw()
    pygame.display.update()
    pygame.time.delay(100)


def draw():
    render_font(screen)
    pos = left = 5
    for idx, i in enumerate(arr):
        pygame.draw.rect(
            screen, arr_color[idx], (left, 105, rect_width-3, i*7))
        left = pos + rect_width
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
        arr_color[i] = PURPLE
        arr_color[j] = PURPLE
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= l_end:
        arr_color[i] = RED
        refill()
        arr_color[i] = PURPLE
        temp.append(arr[i])
        i += 1

    while j <= r_end:
        arr_color[j] = RED
        refill()
        arr_color[j] = PURPLE
        temp.append(arr[j])
        j += 1

    k = 0
    for i in range(l_start, r_end+1):
        pygame.event.pump()
        arr[i] = temp[k]
        k += 1
        arr_color[i] = GREEN
        refill()
        if r_end-l_start == len(arr) - 1:
            arr_color[i] = BLUE
        else:
            arr_color[i] = PURPLE


if __name__ == "__main__":
    HEIGHT = 600
    WIDTH = 810

    # Screen Colors
    WHITE = (255, 255, 255)
    RED = (255, 62, 77)
    BLUE = (10, 121, 223)
    GREEN = (0, 230, 64)
    PURPLE = (60, 64, 198)
    BLACK = (25, 42, 86)
    arr = generate_array(10, 55, 50)
    arr_color = [PURPLE for _ in range(len(arr))]
    screen = prepare_screen()
    rect_width = (WIDTH-10) // len(arr_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
                refill()
                key = pygame.key.get_pressed()
                if key[pygame.K_q]:
                    pygame.quit()
                    quit()
                if key[pygame.K_RETURN]:
                    sort(arr, 0, len(arr)-1)
                    refill()
                if key[pygame.K_g]:
                    arr = generate_array(10, 50, 20)
                    arr_color = [PURPLE for _ in range(len(arr))]
                    refill()
