
# -*- coding: utf-8 -*-
import random
import pygame

# 초기화
pygame.init()



# 화면크기설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 (제목장)
pygame.display.set_caption("못난놈 잘난놈 못된놈 잘된놈 못말리는놈 잘말리는놈 피하기")

# FPS
clock = pygame.time.Clock()

# 이동속도 고정
chaaracter_speed = 1
enemy1_speed = 4
enemy2_speed = 4
enemy3_speed = 4
enemy4_speed = 4

# 이미지 불러오기 (배경)
bg = pygame.image.load("pygame/source/bg2.png")

# 스프라이트 불러오기
character = pygame.image.load("pygame/source/character.png")

# 스프라이트의 크기와 좌표 세팅
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2 )
character_yPos = (screen_height / 2) - (character_height / 2)

# 적군 불러오기
enemy1 = pygame.image.load("pygame/source/enemy.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_xPos = random.randint(0, (screen_width - enemy1_width))
enemy1_yPos = 0

enemy2 = pygame.image.load("pygame/source/enemy.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_xPos = random.randint(0, (screen_width - enemy2_width))
enemy2_yPos = (screen_height + enemy2_height)

enemy3 = pygame.image.load("pygame/source/enemy.png")
enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_xPos = 0
enemy3_yPos = random.randint(0, (screen_height - enemy3_height))

enemy4 = pygame.image.load("pygame/source/enemy.png")
enemy4_size = enemy4.get_rect().size
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_xPos = screen_width - enemy4_width
enemy4_yPos = random.randint(0, (screen_height - enemy4_height))

# 폰트 정해주기
game_font40 = pygame.font.Font(None, 40)
game_font20 = pygame.font.Font(None, 20)

# 게임제한시간
total_time = 0

# 시작시간 정보
start_ticks = pygame.time.get_ticks()

to_x = 0
to_y = 0

# 이벤트 루프 - 종료까지 대기
running = True
while running:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_xPos += to_x * dt
    character_yPos += to_y * dt

# 가로 스크린내 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width

# 세로 스크린내 안벗어나게
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    enemy1_yPos += enemy1_speed
    if enemy1_yPos > screen_height:
        enemy1_yPos = 0
        enemy1_speed = random.randint(1, 3)
        enemy1_xPos = random.randint(0, screen_width - enemy1_width)

    enemy2_yPos -= enemy2_speed
    if enemy2_yPos < 0:
        enemy2_yPos = screen_height - enemy2_height
        enemy2_speed = random.randint(1, 3)
        enemy2_xPos = random.randint(0, screen_width - enemy2_width)

    enemy3_xPos += enemy3_speed
    if enemy3_xPos > screen_width - enemy3_width:
        enemy3_xPos = 0
        enemy3_speed = random.randint(1, 3)
        enemy3_yPos = random.randint(0, screen_height - enemy3_height)

    enemy4_xPos -= enemy4_speed
    if enemy4_xPos < 0:
        enemy4_xPos = screen_width - enemy4_width
        enemy4_speed = random.randint(1, 3)
        enemy4_yPos = random.randint(0, screen_height - enemy4_height)


        
# 충돌 처리하기
    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_xPos
    enemy1_rect.top = enemy1_yPos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_xPos
    enemy2_rect.top = enemy2_yPos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_xPos
    enemy3_rect.top = enemy3_yPos

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_xPos
    enemy4_rect.top = enemy4_yPos

# 충돌 이벤트 체크
    if character_rect.colliderect(enemy1_rect) or character_rect.colliderect(enemy2_rect) or character_rect.colliderect(enemy3_rect) or character_rect.colliderect(enemy4_rect):
        print("충돌! 충돌!")
        running = False


    # screen.fill((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy1, (enemy1_xPos, enemy1_yPos))
    screen.blit(enemy2, (enemy2_xPos, enemy2_yPos))
    screen.blit(enemy3, (enemy3_xPos, enemy3_yPos))
    screen.blit(enemy4, (enemy4_xPos, enemy4_yPos))

    pygame.display.update()
# 종료처리
pygame.quit()






# 종료처리
pygame.quit()