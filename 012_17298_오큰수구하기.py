N = int(input())
A = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]: # 오큰수 조건
        answer[stack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

result = ""
for i in range(N):
    result += str(answer[i]) + " "

print(result)

