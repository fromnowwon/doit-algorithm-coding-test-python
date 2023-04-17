# n에 과목 수를 입력한다
# mylist에 점수 정보를 저장한다
# mymax에 최댓값을 저장한다
# sum에 합을 저장한다
# sum / mymax * 100 / n

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)
print((sum / mymax * 100) / int(n))