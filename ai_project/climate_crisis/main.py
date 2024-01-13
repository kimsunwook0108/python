import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chapter 1: Falling Hail")

# 이미지 로드
hero_image = pygame.image.load("ai_project/climate_crisis/source/hero-removebg-preview.png")
hero_image = pygame.transform.scale(hero_image, (100, 100))  # 이미지 크기 조절

hail_image = pygame.image.load("ai_project/climate_crisis/source/hail-removebg-preview.png")
hail_image = pygame.transform.scale(hail_image, (30, 30))  # 우박 이미지 크기 조절

# 색상 정의
white = (255, 255, 255)

# 우박 리스트 초기화
hail_list = []

# 주인공 초기 위치
hero_x = screen_width // 2 - 25
hero_y = screen_height - 70

# 우박 생성 함수
def create_hail():
    hail_size = random.randint(100, 200)
    hail_x = random.randint(0, screen_width)
    hail_y = -hail_size
    hail_speed = random.uniform(5, 20)
    return {"image": hail_image, "rect": hail_image.get_rect(topleft=(hail_x, hail_y)), "speed": hail_speed}

# 게임 루프
clock = pygame.time.Clock()
spawn_counter = 0  # 우박 생성 주기를 제어하기 위한 카운터
spawn_rate = 60    # 초당 우박 생성 주기

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 배경 색상 설정
    screen.fill(white)

    # 주인공 그리기
    screen.blit(hero_image, (hero_x, hero_y))

    # 우박 생성 및 이동
    spawn_counter += 1
    if spawn_counter >= spawn_rate:
        for _ in range(3):  # 우박을 3배씩 많이 생성
            hail_list.append(create_hail())
        spawn_counter = 0

    for hail in hail_list:
        screen.blit(hail["image"], hail["rect"])
        hail["rect"].y += hail["speed"]

        # 우박이 화면을 벗어나면 리스트에서 제거
        if hail["rect"].y > screen_height:
            hail_list.remove(hail)

    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(30)
