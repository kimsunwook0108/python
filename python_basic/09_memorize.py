import random
eng = []
kor = []
score = 0
order = 0

for i in range(10):
    eng.append(input("단어를 입력하세요 : "))
    kor.append(input("뜻을 입력하세요 : "))

print("10개의 단어를 입력하셨습니다/n이제부터 단어시험을 시작합니다.")

while len(eng) > 0:
    
    order = random.randint(0, len(eng) - 1)
    if eng[order] == input(f"kor[order]은/는 영어로 무엇일까요? : "):
        eng.pop(order)
        kor.pop(order)
        print("축하합니다")
    else:
        print("축하합니다 틀리셨어요")
    
    score += 1

if score == 10:
    print("사람이군")








