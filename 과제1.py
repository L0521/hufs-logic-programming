number = []
for i in range(5):
    num = int(input())
    number.append(num)

number.sort()

sec = number[-2]
print("2번째로 높은 숫자: ", sec)