import random
rcp = ["가위" , "바위", "보"]
user = 0
robot = 0
result = 0

def result_show(who):
    if who == 1:
        return "우리 비겼네"
    elif who == 2:
        return "니가 이겼네?"
    elif who == 3:
        return "니가 졌네?"
def gababo():
    user = input("가위,바위,보 중 하나 골라 : ")
    # robot = rcp[random.randinit(o, 2)]
    robot = random.choice(rcp)

    if user == robot:
        result = 1
    elif user == "가위":
        if robot == "보":
            result = 2    
        else:
            result = 3
    elif user == "바위":
        if robot == "가위":
            result = 2
        else:
            result = 3
    elif user == "보":
        if robot == "바위":
            result = 2
        else:
            result = 3

    print(result_show(result))
    print(f"user : {user}, robot : {robot}")



