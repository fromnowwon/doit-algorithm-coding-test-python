# n값 받기
# numbers에 숫자를 list에 저장한다.
# sum 선언
# for numbers 탐색: sum 변수에 numbers에 있는 각 자릿수를 가져와 더하기

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)
