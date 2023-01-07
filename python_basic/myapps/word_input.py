import time
import os
clear = lambda: os.system('cls')
import random

mode = 0

def word_in():
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

def test():
    kor = open("kor.txt", "r", encoding="UTF-8")
    eng = open("eng.txt", "r", encoding="UTF-8")

    kor_words = []
    eng_words = []

    for r in kor_words.readlines():
        kor_words.append(r.strip())
    for s in eng_words.readlines():
        eng_words.append(s.strip())

    questions = ""
    answer = ""

    for num in range(len(kor_words)):
        questions = kor_words[num]
        clear
        answer = input(f"{questions} 뜻을 적으세요 : ")
        if eng_words[num] == answer:
            print("굳")
        else:
            print("아니야")
        time.sleep(1)
    kor.close()
    eng.close()


def sel():
    while True:
        made = int(input("1 단어 입력, 2 단어 시험, 3 종류"))
        if mode == 3:
            break
        elif mode == 1:
            word_in()
        elif mode == 2:
            test()
        else:
            print("그거 아니야 돌아가")