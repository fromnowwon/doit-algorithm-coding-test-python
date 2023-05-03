import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort() #정렬

for k in range(N):
    find = A[k]
    i = 0 # 맨앞
    j = N - 1 # 맨뒤
    while i < j: # 투포인터 알고리즘
        if A[i] + A[j] == find: # find는 서로 다른 두 수의 합
            if i != k and j != k:
                Result += 1
                break
            elif i == k: # k에 i포인터가 와있는 경우 포인터 변경 및 계속 수행
                i += 1
            elif j == k: # k에 j포인터가 와있는 경우 포인터 변경 및 계속 수행
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(Result)


