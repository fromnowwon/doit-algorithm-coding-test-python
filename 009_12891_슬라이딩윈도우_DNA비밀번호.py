# 전역 변수 선언
checkList = [0] * 4 # [0, 0, 0, 0]
myList = [0] * 4 # [0, 0, 0, 0]
checkSecret = 0 # 몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수


# 함수 정의
def myadd(c): # 새로 들어온 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1 # 리스트 첫 번째에 개수 추가
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1 # 리스트 두 번째에 개수 추가
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1 # 리스트 세 번째에 개수 추가
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1 # 리스트 네 번째에 개수 추가
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): # 제거되는 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)