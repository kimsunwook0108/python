# import random

# drgon_chair = ["dragon", "선생", "님", "drgon slayer"]
# bam = ["f", "u", "c", "k"]
# bam_toll = ["코딩", "코딩쌤", "코딩학원", "키보드"]
# a = random.choice(drgon_chair)
# b = random.choice(bam)
# c = random.choice(bam_toll)

# print(f"용의자 {a}가 {b}에서 {c}으로 선생님을 살해했다.")


def deotsem(number):
    sum = 0
    for i in range(number):
        sum += (i + 1)
    print(sum)
    return sum
deotsem(deotsem(15))