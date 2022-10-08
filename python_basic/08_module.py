import random
from split_04 import *
from lotto_06 import lotto1
import fortuneteller_07 as f

select = 0

running = True
while running:
    select = int(input('''안녕하세요 주인님. 무엇을 실행할까요?
1.계산기 2.로또번호 추첨기 3.미래배우자 예언 4.끝
(위의 앱 중 하나를 번호로 선택하시요) : '''))

    if select == 4:
        break
    elif select == 2:
        lotto1()
    elif select == 1:
        f.future()
    elif select == 1:
        print(myname)
        calculator()

print("너 별로야")
