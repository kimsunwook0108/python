from this import d


myname = "김선욱"

def calculator():

    result = 0
    input_data = 0


    while True:
        input_data = input("계산 식 : ")
        if "+" in input_data:
            result = int(input_data.split("+")[0]) + int(input_data.split("+")[1])
        elif "-" in input_data:
            result = int(input_data.split("-")[0]) - int(input_data.split("-")[1])
        elif "*" in input_data:
            result = int(input_data.split("*")[0]) * int(input_data.split("*")[1])
        elif "/" in input_data:
            result = int(input_data.split("/")[0]) / int(input_data.split("/")[1])
        elif "꺼져" in input_data:
            print("빵빠레")
            break
        else:
            print("빵빠레 먹을래?")
            continue
        print(f"{input_data} = {result}")