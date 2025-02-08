import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pyttsx3

def display_message(text):
    # Create a black image
    black_screen = np.zeros((480, 640, 3), dtype=np.uint8)
    # Convert to PIL image
    pil_image = Image.fromarray(black_screen)
    draw = ImageDraw.Draw(pil_image)
    # Load a font
    font_path = "C:/Windows/Fonts/malgun.ttf"  # Ensure you have a Korean font installed
    font = ImageFont.truetype(font_path, 32)
    # Get text size
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    # Calculate text position
    textX = (black_screen.shape[1] - text_width) // 2
    textY = (black_screen.shape[0] - text_height) // 2
    # Add text to image
    draw.text((textX, textY), text, font=font, fill=(255, 255, 255))
    # Convert back to OpenCV image
    black_screen = np.array(pil_image)
    # Display the image
    cv2.imshow('Face Detection', black_screen)

def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# 웹캠 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        display_message("입장 가능")
    elif len(faces) == 2:
        speak_message("한명씩 입장해주세요")
        display_message("한명씩 입장하세요")
    elif len(faces) == 1:
        speak_message("어서오세요")
        # 얼굴에 사각형 그리기
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 결과 프레임 표시
        cv2.imshow('Face Detection', frame)
    else:
        # 얼굴에 사각형 그리기
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 결과 프레임 표시
        cv2.imshow('Face Detection', frame)

    # 'q'키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 해제 및 닫기
cap.release()
cv2.destroyAllWindows()