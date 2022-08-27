ban_dict = ["개새끼, 씨발, 병신, 미친놈"]

status = True

print("챗봇을 시작합니다")
while status:
    bad_words = 0
    chat = input("말씀하세요 주인님 : ")
    for word in ban_dict:
        if word in chat:
            bad_words += 1
    if chat == "꺼져":
        status = False    
    if bad_words == 0:
        print("맞아요. 주인님")
    else:
        print("착한어린이는 그런말 쓰면 안돼요.")
    
print("꺼질게요. 안녕히게세요.")







