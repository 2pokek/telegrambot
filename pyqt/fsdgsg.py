import pygame
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Snake')

game_over = False

x1 = [300]
y1 = [400]

food_x = random.randint(0, 80) * 10
food_y = random.randint(0, 50) * 10

x1_change = 0
y1_change = 0
n = 1
score = 0

clock = pygame.time.Clock()
time = 10


def print_text(text):
    font = pygame.font.SysFont(None, 20, True, False)
    surface = font.render(text, True, (0, 0, 0))
    dis.blit(surface, (10, 10))


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1[0] >= 800 or x1[0] < 0 or y1[0] < 0 or y1[0] > 500:
        game_over = True

    if x1[0] == food_x and y1[0] == food_y:
        food_x = random.randint(0, 80) * 10
        food_y = random.randint(0, 50) * 10
        x1.append(x1[-1])
        y1.append(y1[-1])
        n += 1
        time += 1
        score += 1

    a = x1[0]
    b = y1[0]
    x1[0] += x1_change
    y1[0] += y1_change
    dis.fill(white)
    print_text(f'Total score: {score}')

    for i in range(n):
        if i != 0:
            x1[i], a = a, x1[i]
            y1[i], b = b, y1[i]
        pygame.draw.rect(dis, blue, [x1[i], y1[i], 10, 10])

    pygame.draw.rect(dis, red, [food_x, food_y, 10, 10])
    pygame.display.update()
    clock.tick(time)

pygame = quit()
quit()
