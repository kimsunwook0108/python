number_a = 0
symbol = 0
number_b = 0
result = 0
input_data = 0

number_a = int(input("숫자 a를 입력하세요 : "))
symbol = input("+, -, *, / 중 하나를 입력하세요 : ")
number_b = int(input("숫자 b를 입력하세요 : "))

if symbol == "+":
    result = number_a + number_b
if symbol == "-":
    result = number_a - number_b
if symbol == "*":
    result = number_a * number_b
if symbol == "/":
    result = number_a / number_b

print(f"{number_a} {symbol} {number_b} = {result}")
