import random

bab = ["가위", "바위", "보"]
user = 0
mony = 0
# running = True

while user == "q":
    user = input("골라 : ")
    mony = random.choice(bab)
    if bab == user:
        print("비겼네")
    else:
        if user == "가위":
            if mony == "바위":
                print(f"사람{user}, 컴{mony} ==> 컴 승 ") 
            else:
                print(f"사람{user}, 컴{mony} ==> 사람 승 ") 
        if user == "보":     
            if bab == "가위":   
                print(f"사람{user}, 컴{mony} ==> 컴 승 ") 
            else:
                print(f"사람{user}, 컴{mony} ==> 사람 승 ") 
        if user == "바위":     
            if bab == "보":   
                print(f"사람{user}, 컴{mony} ==> 컴 승 ") 
            else:
                print(f"사람{user}, 컴{mony} ==> 사람 승 ") 