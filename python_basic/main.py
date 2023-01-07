'''
1.단어 암기장 = word_input.py
2.로또번호 추첨기 = lotto_06.py
3.나쁜말 탐지기 = data_if.py
4.계산기 = calculator.py
5.가위바위보 = funcition.py
''' 
select = 0

from myapps import word_input
from myapps import lotto_06
from myapps import data_if
from myapps import calculator
from myapps import funcition



print("=" + 20)
print("앱 모음")
print("1. 영단어 암기장\n2, 2. 로또번호 추첨기\n3, 3. 나쁜말 탐지기\n4, 4.계산기\n5 5. 가위바위보\n6")
print("=" + 20)
select = input("하나를 골라 번호를 쓰세요 : ")