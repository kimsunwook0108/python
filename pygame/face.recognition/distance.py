import serial
import pygame
import sys
import cv2

# # Pygame 초기화
# pygame.init()
# font = pygame.font.Font(None, 36)

# # 화면 설정
# WIDTH = 800
# HEIGHT = 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("거리 측정기")

# 시리얼 통신 설정
try:
    arduino = serial.Serial('COM5', 9600)
except serial.SerialException:
    print("아두이노 연결 실패")
    sys.exit(1)

# 웹캠 초기화
cap = cv2.VideoCapture(0)
webcam_active = False
 
# # 원 설정
# MAX_RADIUS = 300    # 최대 원 반지름
# MIN_RADIUS = 50     # 최소 원 반지름
# BASE_DISTANCE = 30  # 기준 거리
# SMOOTHING = 0.3     # 원 크기 변화 부드러움 정도
# current_radius = MAX_RADIUS

running = True
while running:
    # # 이벤트 처리
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    
    # 거리 데이터 읽기
    if arduino.in_waiting:
        distance = int(arduino.readline().decode().strip())
        # print(f"현재 거리: {distance}cm")
        
        # 웹캠 제어 (150cm 기준)
        if distance <= 50 and not webcam_active:
            cap.open(0)
            webcam_active = True
        elif distance > 50 and webcam_active:
            cap.release()
            webcam_active = False
        
        # 웹캠 화면 표시
        if webcam_active:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('웹캠', frame)
                cv2.waitKey(1)
        else:
            cv2.destroyAllWindows()
        
        # # 거리에 따른 원 크기 계산
        # target_radius = int(MAX_RADIUS * (BASE_DISTANCE / max(distance, 1))**0.8)
        # target_radius = max(min(target_radius, MAX_RADIUS), MIN_RADIUS)
        # current_radius = int(current_radius * (1 - SMOOTHING) + target_radius * SMOOTHING)
        
        # # 화면 그리기
        # screen.fill((0, 0, 0))  # 검은색 배경
        # pygame.draw.circle(screen, (255, 255, 255), (WIDTH//2, HEIGHT//2), current_radius)
        
        # # 거리 정보 표시
        # text = font.render(f'distance: {distance}cm', True, (0, 255, 0))
        # screen.blit(text, (10, 10))
        
        # pygame.display.flip()

# 프로그램 종료 시 정리
cap.release()
cv2.destroyAllWindows()
arduino.close()
# pygame.quit()
sys.exit()



# 아두이노 코드
# const int trigPin = 9;
# const int echoPin = 10;

# void setup() {
#   Serial.begin(9600);
#   pinMode(trigPin, OUTPUT);
#   pinMode(echoPin, INPUT);
# }

# void loop() {
#   digitalWrite(trigPin, LOW);
#   delayMicroseconds(2);
#   digitalWrite(trigPin, HIGH);
#   delayMicroseconds(10);
#   digitalWrite(trigPin, LOW);
  
#   long duration = pulseIn(echoPin, HIGH);
#   int distance = duration * 0.034 / 2;
  
#   Serial.println(distance);
#   delay(100);
# }