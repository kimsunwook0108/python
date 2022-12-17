import random

numbers = []
running = True
count = 0

for i in range(10):
    numbers.append(random.randint(1, 100))

while running:
    move = 0
    for i in range(len(numbers)-1):
        if numbers[i] <= numbers[i]:
            numbers[i], numbers[i + 1] = numbers[i+1], numbers[i]
            move += 1
            count += 1
    if move == 0:
        running = False
print(numbers)
print(numbers, f"정렬한 횟수 : {count}")

# for d in range(100):
#     if numbers[0] <= numbers[1]:
#         numbers[0], numbers[1] = numbers[1], numbers[0]
#     if numbers[1] <= numbers[2]:
#         numbers[1], numbers[2] = numbers[2], numbers[1]
#     if numbers[2] <= numbers[3]:
#         numbers[2], numbers[3] = numbers[3], numbers[2]
#     if numbers[3] <= numbers[4]:
#         numbers[3], numbers[4] = numbers[4], numbers[3]
#     if numbers[4] <= numbers[5]:
#         numbers[4], numbers[5] = numbers[5], numbers[4]
#     if numbers[5] <= numbers[6]:
#         numbers[5], numbers[6] = numbers[6], numbers[5]
#     if numbers[6] <= numbers[7]:
#         numbers[6], numbers[7] = numbers[7], numbers[6]
#     if numbers[7] <= numbers[8]:
#         numbers[7], numbers[8] = numbers[8], numbers[7]
#     if numbers[8] <= numbers[9]:
#         numbers[8], numbers[9] = numbers[9], numbers[8]

# print(numbers)