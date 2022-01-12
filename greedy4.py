n, k=map(int, input('N과 K를 설정하세요: ').split())

cnt=0

while(n!=1):
    if(n%k==0):
        n = n/k
        cnt += 1
    elif(n%k!=0):
        n -= 1
        cnt += 1
print(cnt)