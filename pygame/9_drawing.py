import pygame
import random
pygame.init()

# 화면크기설정
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 (제목장)
pygame.display.set_caption("뱀")

# 이벤트 루프 - 종료까지 대기
clock = pygame.time.Clock()

r = 20
running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 배경설정
    screen.fill((255, 255, 255))

# 선그리기2
    # measure = screen_width / 10

    # for i in range(10):
    #     pygame.draw.line(screen, (0, 0, 0), (0, i * measure), (screen_width, i * measure), 2)
    #     pygame.draw.line(screen, (0, 0, 0), (i * measure, 0), (i * measure, screen_width), 2)


# 직선그리기 1
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (1 / 10), 0), (screen_width * (1 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (2 / 10), 0), (screen_width * (2 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (3 / 10), 0), (screen_width * (3 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (4 / 10), 0), (screen_width * (4 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (5 / 10), 0), (screen_width * (5 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (6 / 10), 0), (screen_width * (6 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (7 / 10), 0), (screen_width * (7 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (8 / 10), 0), (screen_width * (8 / 10), screen_height), 2)
    # pygame.draw.line(screen, (0, 0, 0), (screen_width * (9 / 10), 0), (screen_width * (9 / 10), screen_height), 2)


    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (1 / 10)), (screen_width, screen_height * (1 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (2 / 10)), (screen_width, screen_height * (2 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (3 / 10)), (screen_width, screen_height * (3 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (4 / 10)), (screen_width, screen_height * (4 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (5 / 10)), (screen_width, screen_height * (5 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (6 / 10)), (screen_width, screen_height * (6 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (7 / 10)), (screen_width, screen_height * (7 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (8 / 10)), (screen_width, screen_height * (8 / 10)), 2)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height * (9 / 10)), (screen_width, screen_height * (9 / 10)), 2)


# 원 그리기


    # pygame.draw.circle(screen, (0, 255, 100), (screen_width / 2, screen_height / 2), 100)
    # pygame.draw.circle(screen, (255, 0, 0), (screen_width / 2, screen_height / 2), r, 5)
    # r += 10
    # if r > 250:
    #     r = 20

# 사각형 그리기
    # pygame.draw.rect(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 100))
    pygame.draw.rect(screen, (55, 55, 255), (screen_width / 2 , screen_height / 2, r, r), 5)
    r += 10
    if r > 250:
        r = 20

    pygame.display.update()

# 종료처리
pygame.quit()