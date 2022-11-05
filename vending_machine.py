drinks = {"콜라" : 1400, "사이다" : 1400, "환타" : 1300, "포카리스웨트" : 1200, "파워에이드" : 1300}
money = 0
customer = True
chdice = 0
income = 0

def display():
    print("=" * 22)
    print("=" * 5, "독약 자판기", "=" * 5)
    print(drinks)
    print("=" * 22)
    print(f"잔액 : {money}")
    print("=" * 22)

while True:
    customer = True
    while customer:
        display()
        select = int(input("1. 돈넣기 / 2. 물건사기 / 3. 나가기 : "))
        if select == 1:
            money = int(input("금액 입력 : "))
            continue
        elif select ==2:
            display()
            choice = input("상품을 고르세요 : ")
            if money >= drinks[choice]:
                print(f"***{choice} 상품 구매 완료***")
                income += drinks[chdice]
                money = money - drinks[choice]
            else:
                print("돈 더 가져와")
                break
        elif select ==3:
            print("***수고링***")
            if money > 0 :
                print(f"***환불금액 : {money}***")
                money = 0
                customer = False
        elif select == 1704:
            print(f"***오늘의 수익 : {income}***")
            input("부자되세요 주인님!")
        else:
            print("잘못누르셨습니다")