from collections import deque
N = int(input())
Q = deque()

for i in range(1, N+1):
    Q.append(i)

while len(Q) > 1:
    Q.popleft() # 맨 위 카드 버림
    Q.append(Q.popleft()) # 맨 위 카드 맨 뒤에 붙임

print(Q[0])