# -*- coding: utf-8 -*-
import random
import pygame
pygame.init()

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 (제목장)
pygame.display.set_caption("못난놈 잘난놈 못된놈 잘된놈 못말리는놈 잘말리는놈 피하기")

# 이미지 불러오기 (배경)
bg = pygame.image.load("pygame/source/bg.png")

# 스프라이트 불러오기
character = pygame.image.load("pygame\source\character.png")

# 스프라이트의 크기와 좌표 세팅
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_xPos = (screen_width / 2) - (character_width / 2 )
character_yPos = screen_height - character_height

# 이벤트 루프 - 종료까지 대기
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    pygame.display.update()
# 종료처리
pygame.quit()