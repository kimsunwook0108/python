import pygame
import sys
import random
import math

# Pygame 초기화
pygame.init()

# 창 크기 설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating and Scaling Images")

# 배경 이미지 로드
background_image = pygame.image.load("pygame/source/bg4.jpg")  # 배경 이미지 파일 경로를 적절히 수정하세요

# 이미지 로드
original_image = pygame.image.load("pygame/source/image.png")  # 이미지 파일 경로를 적절히 수정하세요

# 이미지 크기 조절
scale_factor = 0.2  # 이미지 크기를 조절하는 비율
image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))

# 이미지 회전 함수
def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect().center)
    return rotated_image, new_rect

# 객체 클래스 정의
class RotatingObject:
    def __init__(self, image, x, y):
        self.image = image
        self.angle = 0
        self.rotated_image, self.rect = rotate_image(self.image, self.angle)
        self.rect.topleft = (x, y)
        self.speed = 1  # 이동 속도
        self.rotation_speed = 1  # 회전 속도

    def update(self):
        self.angle += self.rotation_speed  # 회전 각도 증가
        self.rotated_image, self.rect = rotate_image(self.image, self.angle)
        self.rect.y += self.speed  # y 좌표 증가

# RotatingObject 인스턴스 생성
objects = []
for _ in range(10):  # 10개의 무작위로 생성된 객체
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    new_object = RotatingObject(image, x, y)
    objects.append(new_object)

# 게임 루프
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 객체 업데이트
    for obj in objects:
        obj.update()

    # 배경 그리기
    screen.blit(background_image, (0, 0))

    # 객체 그리기
    for obj in objects:
        screen.blit(obj.rotated_image, obj.rect.topleft)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 제한
    clock.tick(60)




