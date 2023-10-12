#1과 10 사이의 수를 두 번 받아서 그중 더 큰 수의 숫자만큼 별표로 나타내기
def fnum(num1,num2):
  if num1 > num2 :
    return num1
  else :
    return num2

num1 = int(input())
num2 = int(input())

res = fnum(num1,num2)

if 1 <= res <= 10:
    print("*" * res)
else :
    print("1과 10 사이의 수를 입력하세요.")