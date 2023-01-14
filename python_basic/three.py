def korea():
    name = ""
    name10 = []
    name_in = ""

    name = input("글자 입력 : ")
    for i in name:
        name_in = input(f"{i} : ")
        while True:
            if i == name_in[0]:
                name10.append(name_in)
                break
            else:
                print("첫글자 안맞음 다시해")
    print("=" * 30)
    print(f"{name} 으로 만든 글")
    for w in range(len(name)):
        print(f"{name[w]} : {name10[w]}")
    print("="* 30)

    return name10
f = open("event.txt", "a", encoding="UTF-8")
for e in korea():
    f.writ(e="\n")
f.close()