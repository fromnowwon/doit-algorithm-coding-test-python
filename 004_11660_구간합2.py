import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0] * (n + 1)] # 원본 배열 초기화 [[0, 0, 0, 0]]
D = [[0] * (n + 1) for _ in range(n + 1)] # 합배열 초기화 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 원본 배열 받기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합배열 구하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

# 질의 답변
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x2-1][y1] - D[x1][y2-1] + D[x1-1][y1-1]
    print(result)