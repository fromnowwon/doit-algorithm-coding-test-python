N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i] # 수열값
    if su > num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        # 새로 들어가야 하는 수열값이 오름차순으로 들어오는 자연수보다 작아진 경우 pop가능
        stack.pop()
        answer += "-\n"
    else:
        top = stack.pop()
        if top > su: # 스택 맨 위 값이 새로 들어가야 하는 수열 값보다 큰 경우
            print("NO") # 스택에 수열 값을 넣을 수 없다
            result = False
            break
        else:
            answer += "-\n"
if result:
    print(answer)

