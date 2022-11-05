sajeon = {"apple" : "사과", "friend" : "친구", "aori" : "사과"}

print(sajeon["apple"])
print(sajeon["aori"])
print(sajeon.keys())
print(sajeon.values())
print(sajeon.items())
print("apple" in sajeon)
print("ant" in sajeon)

naver = {"정시우" : ["남자", "양일중", "브롤짱", "자전거"], "김선욱" : ["남자", "지평중", "겜알못", "도보"], "김시우" : ["남자", "구라중", "탕탕찐", "지하철"]}

if "김시우" in naver:
    print(naver["정시우"])
else:
    print("없어요")

naver["코딩썜"] = ["남자", "코드플레이", "잘생김", "자가용"]
print(naver)



# del naver["코딩쌤"]
# del naver["coding3"]
print(naver)


sajeon.update(naver)
print(sajeon)
print(naver)

