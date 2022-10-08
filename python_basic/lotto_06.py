import random

def lotto1():

    lotto_numbers = []
    lotto_picks = []
    pick = 0

    for i in range(45):
        lotto_numbers.append(i + 1)
    for j in range(7):
        pick = lotto_numbers.pop(random.randint(0, len(lotto_numbers) - 1))
        lotto_picks.append(pick)

    print(f"예상번호{lotto_picks}") 
    print(lotto_numbers)