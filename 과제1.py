#숫자를 5번 입력 받아서 정렬한 뒤, 두번 째로 높은 숫자 찾기
number = []
for i in range(5):
    num = int(input())
    number.append(num)

number.sort()

sec = number[-2]
print("2번째로 높은 숫자: ", sec)
