n,m=map(int, input('행과 열의 크기를 설정하세요: ').split())
data=[]
answer=0
compared=[]
for i in range(n):
    data.append(list(map(int, input('행을 순서대로 입력해주세요: ').split())))
    compared.append(min(data[i]))
    answer=max(compared)

print(answer)