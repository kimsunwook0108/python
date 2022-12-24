kor = open("kor.txt", "a", encoding="UTF-8")
eng = open("eng.txt", "a", encoding="UTF-8")
answer = 0
while True:
    answer = input("입력은 a, 나가기는 q : ")
    if answer == "q":
        break
    if answer == "a": 
        in_kor = input("한글 입력 : ")
        in_eng = input("영어 입력 : ")
        kor.write(f"{in_kor}\n")
        eng.write(f"{in_eng}\n")
kor.close()
eng.close()