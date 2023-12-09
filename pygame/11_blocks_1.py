# -*- coding: utf-8 -*-
import random
import pygame
pygame.init()

# 화면크기설정
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 (제목장)
pygame.display.set_caption("벽동깨기")

# 막대기 정의
bar_width = 150
bar_height = 25

bar_xpos = screen_width / 2 - bar_width / 2
bar_Ypos = screen_height - bar_height
bar_rect = pygame.Rect(bar_xpos, bar_Ypos, bar_width, bar_height)

# 공 정의
ball_size = 20

ball_Xpos = screen_width / 2
ball_Ypos = screen_height - bar_height - ball_size

ball_rect = pygame.Rect(ball_Xpos, ball_Ypos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_Xpos, ball_Ypos)

# 블록 정의
block_width = screen_width / 10
block_height = screen_height / 20

block_Xpos = 0
block_Ypos = 0

blocks = [[] for _ in range(10)]
block_color = [[] for _ in range(10)]

for i in range(10):
    for j in range(3):
        blocks[i].append(pygame.Rect(i*block_width, j*block_height, block_width, block_height))
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256)))


# 이벤트 루프 - 종료까지 대기
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((200, 200, 100))
    pygame.draw.rect(screen, (90, 90, 255), bar_rect)
    pygame.draw.circle(screen, (90, 90, 255), (ball_Xpos, ball_Ypos), ball_size)

    for i in range(10):
        for j in range(3):
            pygame.draw.rect(screen, block_color[i][j], blocks[i][j])

    pygame.display.update()
# 종료처리
pygame.quit()
