# 구간의 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sumArray = [0]
temp = 0

# 합배열 만들기
for i in numbers:
    temp += i
    sumArray.append(temp)

# 구간의 합 구하기
for i in sumArray:
    s, e = map(int, input().split())
    print(sumArray[e] - sumArray[s-1])