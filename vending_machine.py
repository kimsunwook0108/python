drinks = {"콜라" : [1400, 10], "사이다" : [1400, 10], "환타" : [1300, 10], "포카리스웨트" : [1200, 10], "파워에이드" : [1300, 10]}
money = 0
customer = True
choice = 0
income = 0
select = 0
name = []
price_stock = []
price = []
stock = []

name = list(drinks.keys())
price_stock = list(drinks.values())
for i in price_stock:
    price.append(i[0])
    stock.append(i[1])

def display():
    print("=" * 23)
    print("=" * 5, "독약 자판기", "=" * 5)
    for j in range(len(name)):
        print(f"{name[j]} - {price[j]}원")
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
            choice = name.index(input("상품을 고르세요 : "))
            if money >= price[choice]:
                if stock[choice] > 0:
                    print(f"***{name[choice]} 상품 구매 완료***")
                    income += price[choice]
                    money -= price[choice]
                    stock[choice] -= 1
                else:
                    print(f"{name[choice]} 음료는 품절입니다")
                    break
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
            print("****음료별 판매 현황****")
            for x in range(len(name)):
                print(f"{name[x]} = {10 - stock[x]}개 판매")
            input("부자되세요 주인님!")
        else:
            print("잘못누르셨습니다")