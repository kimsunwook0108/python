import random

def future():

    outfit = ["예쁨", "잘생김", "못생김", "키큼", "키작음", "둥뚱함", "마름"]
    gender = ["남성", "여성"]
    age = 0
    name = input("당신은 누구싶니까? : ")

    print(f"{name}님 당신의 미래를 예언해 드릴게요.")
    print(f"당신의 배우자는 {random.choice(outfit)} {random.choice(gender)} 모습입니다. 나이는 {random.choice(19, 79)}살 정도로 추정 됨니다.")




