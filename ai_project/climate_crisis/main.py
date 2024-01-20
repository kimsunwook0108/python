import pygame
import sys
import random
import os

# 현재 스크립트의 디렉토리 경로를 가져옵니다.
current_path = os.path.dirname(__file__)

# 화면 설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chapter 1: Falling Hail")

# 이미지 로드
hero_image_path = os.path.join(current_path, "source/hero-removebg-preview-removebg-preview.png")
hero_image = pygame.image.load(hero_image_path)
hero_image = pygame.transform.scale(hero_image, (40, 60))  # 주인공 이미지 크기 조절

hail_image_path = os.path.join(current_path, "source/hail-removebg-preview-removebg-preview.png")
hail_image = pygame.image.load(hail_image_path)  # 사용자 정의 우박 이미지
hail_image = pygame.transform.scale(hail_image, (30, 30))  # 우박 이미지 크기 조절

heart_image_path = os.path.join(current_path, "source/heart-removebg-preview.png")
heart_image = pygame.image.load(heart_image_path)
heart_image = pygame.transform.scale(heart_image, (30, 30))  # 하트 이미지 크기 조절

# 바닥 이미지 생성
ground_image = pygame.Surface((screen_width, 20))
ground_image.fill((0, 255, 0))  # 초록색으로 채워진 바닥 이미지

# 색상 정의
white = (255, 255, 255)

# 우박 리스트 초기화
hail_list = []

# 초기 하트 개수 설정
heart_count = 3

# 바닥 설정
ground_rect = ground_image.get_rect()
ground_rect.topleft = (0, screen_height - 20)  # 바닥 위치 (화면 아래에)

# 주인공 초기 위치 (화면 가로 중앙, 화면 밑 바닥)
hero_x = screen_width // 2 - 20
hero_y = screen_height - 60  # 주인공 크기에 맞게 조절

hero_speed = 10  # 주인공 이동 속도
jump_height = 150  # 점프 높이
is_jumping = False  # 점프 중인지 여부를 저장하는 변수

# 키 상태 저장 변수
left_key_pressed = False
right_key_pressed = False
space_key_pressed = False

# 점프 가능 여부를 나타내는 변수
jump_available = True
jump_cooldown = 0  # 점프 쿨다운 카운터

# 하트 초기 위치 설정
heart_positions = [(10, 10), (50, 10), (90, 10)]

# 우박 생성 함수
def create_hail():
    hail_size = random.randint(30, 100)  # 크기를 랜덤하게 설정 (30에서 100 사이)
    hail_x = random.randint(0, screen_width)
    hail_y = -hail_size
    hail_speed = random.uniform(5, 20)
    return {"image": pygame.transform.scale(hail_image, (hail_size, hail_size)), "rect": pygame.Rect(hail_x, hail_y, hail_size, hail_size), "speed": hail_speed}

# 게임 루프
clock = pygame.time.Clock()
spawn_counter = 0  # 우박 생성 주기를 제어하기 위한 카운터
spawn_rate = 30    # 초당 우박 생성 주기
jump_available = True  # 추가적인 점프 입력을 받을 수 있는지 여부

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left_key_pressed = True
            elif event.key == pygame.K_d:
                right_key_pressed = True
            elif event.key == pygame.K_SPACE and not is_jumping and jump_available:
                is_jumping = True
                original_y = hero_y  # 현재 위치를 저장하고 점프 중임을 표시
                jump_available = False  # 점프 중에는 추가적인 점프 입력을 받지 않도록 설정
                jump_cooldown = 30  # 점프 후 쿨다운 설정
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left_key_pressed = False
            elif event.key == pygame.K_d:
                right_key_pressed = False

    # 'a' 키가 눌려있으면 주인공을 왼쪽으로 이동
    if left_key_pressed:
        hero_x -= hero_speed
        # 주인공이 화면 왼쪽 경계를 벗어나지 않도록 제한
        hero_x = max(hero_x, 0)

    # 'd' 키가 눌려있으면 주인공을 오른쪽으로 이동
    if right_key_pressed:
        hero_x += hero_speed
        # 주인공이 화면 오른쪽 경계를 벗어나지 않도록 제한
        hero_x = min(hero_x, screen_width - 40)  # 주인공 이미지의 가로 크기만큼 빼줌

    # 스페이스바를 눌렀을 때 점프
    if is_jumping:
        hero_y -= 10  # 위로 이동
        if hero_y <= original_y - jump_height:
            is_jumping = False  # 점프 높이에 도달하면 점프 종료
    else:
        hero_y += 10  # 아래로 이동
        # 주인공이 바닥을 통과하지 않도록 제한
        hero_y = min(hero_y, screen_height - 60)  # 60은 주인공 이미지의 높이

    # 점프 쿨다운 감소
    jump_cooldown = max(jump_cooldown - 1, 0)

    # 배경 색상 설정
    screen.fill(white)

    # 우박 생성 및 이동
    spawn_counter += 1
    if spawn_counter >= spawn_rate:
        for _ in range(5):  # 우박을 5개씩 많이 생성
            hail_list.append(create_hail())
        spawn_counter = 0

    # 주인공과 우박의 충돌을 체크하는 사각형 생성
    hero_rect = pygame.Rect(hero_x, hero_y, 40, 60)

    # 주인공과 우박 충돌 체크
    for hail in hail_list:
        if hero_rect.colliderect(hail["rect"]):
            # 우박이 주인공에 닿으면 우박이 바로 사라지고 하트 하나가 없어짐
            hail_list.remove(hail)
            if heart_count > 0:
                heart_count -= 1

    for hail in hail_list:
        screen.blit(hail["image"], hail["rect"])
        hail["rect"].y += hail["speed"]

        # 우박이 화면을 벗어나면 리스트에서 제거
        if hail["rect"].y > screen_height:
            hail_list.remove(hail)

    # 바닥 그리기
    screen.blit(ground_image, ground_rect)

    # 하트 그리기
    for i in range(heart_count):
        screen.blit(heart_image, heart_positions[i])

    # 주인공 그리기 (주의: 우박 그리기보다 먼저 그려져야 함)
    screen.blit(hero_image, (hero_x, hero_y))

    pygame.display.flip()
    clock.tick(30)
