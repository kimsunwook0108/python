# -*- coding: utf-8 -*-

import pygame
pygame.init()

# 화면크기설정
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 (제목장)
pygame.display.set_caption("뱀")

circleX_pos = 0
circleY_pos = 0

L_clic = pygame.mixer.Sound("pygame/source/L.wav")
R_clic = pygame.mixer.Sound("pygame/source/R.wav")

clock = pygame.time.Clock()

# 이벤트 루프 - 종료까지 대기
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.MOUSEMOTION:
        print("mousemotion")
        print(pygame.mouse.get_pos())
        circleX_pos, circleY_pos = pygame.mouse.get_pos()
        screen.fill((11, 55, 26))
        pygame.draw.circle(screen, (255, 0, 255), (circleX_pos, circleY_pos), 10)

    if event.type == pygame.MOUSEBUTTONDOWN:
        print("버튼을 누르셨습니다.")
        print(pygame.mouse.get_pos())
        print(event.button)
        if event.button == 1:
            print("좌클")
            L_clic.play()
        elif event.button == 3:
            print("우클")
            R_clic.play()
        elif event.button == 2:
            print("휠클")
        elif event.button == 4:
            print("휠업")
        elif event.button == 5:
            print("우다운")
            
    pygame.display.update()
# 종료처리
pygame.quit()

