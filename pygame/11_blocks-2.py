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
bar_to_X = 0

# 공 정의
ball_size = 20

ball_Xpos = screen_width / 2
ball_Ypos = screen_height - bar_height - ball_size

ball_rect = pygame.Rect(ball_Xpos, ball_Ypos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_Xpos, ball_Ypos)

ball_x_speed = 0.3
ball_y_speed = 0.3

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

# 바와 마우스 움직임 정의
mouse_xPos = 0
mouse_yPos = 0


# 이벤트 루프 - 종료까지 대기
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEMOTION:
        mouse_xPos, mouse_yPos = pygame.mouse.get_pos()
        if mouse_xPos - bar_width / 2 >= 0 and mouse_yPos + bar_width / 2 <= screen_width:
            bar_xpos = mouse_xPos - bar_width / 2
            bar_rect.left = mouse_xPos - bar_width / 2

    screen.fill((200, 200, 100))

# 막대기 그리기
    bar_xpos += bar_to_X

    if bar_xpos< 0:
        bar_xpos = 0
    if bar_xpos > screen_width - bar_width:
        bar_xpos = screen_width - bar_width
    bar_rect.left = bar_xpos

    pygame.draw.rect(screen, (90, 90, 255), bar_rect)

# 공 튕기기
    if ball_Xpos - ball_size <= 0:
        ball_x_speed = -ball_x_speed
    elif ball_Xpos >= screen_width - ball_size:
        ball_x_speed = -ball_x_speed

    if ball_Ypos - ball_size <= 0:
        ball_y_speed = -ball_y_speed
    elif ball_Ypos >= screen_width - ball_size:
        ball_y_speed = -ball_y_speed

    ball_Xpos += ball_x_speed
    ball_Ypos += ball_y_speed
    
    # 공그리기
    ball_rect.center = (ball_Xpos, ball_Ypos)
    pygame.draw.circle(screen, (255, 255, 255), (ball_Xpos, ball_Ypos), ball_size)

    # 막대기 충돌판정 
    if ball_rect.colliderect(bar_rect):
        ball_y_speed *= -1

    # 벽돌 그리기
    for i in range(10):
        for j in range(3):
            if blocks[i][j]:
                pygame.draw.rect(screen, block_color[i][j], blocks[i][j])
                blocks[i][j].topleft = (i * block_width, j * block_height)

                if ball_rect.colliderect(blocks[i][j]):
                    ball_x_speed *= -1
                    ball_y_speed *= -1
                    blocks[i][j] = 0

    pygame.display.update()
# 종료처리
pygame.quit()
