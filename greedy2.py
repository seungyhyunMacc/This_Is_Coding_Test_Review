n,m,k=map(int, input('크기, 횟수, k값 입력하세요: ').split())
data= list(map(int, input('배열을 입력해주세요: ').split()))
data.sort()

count=0;
answer=0;
print(list(data))

BN1=data[n-1]
BN2=data[n-2]

# while(m>0):
#     if(BN1==BN2):
#         answer +=BN1
#         m-=1
#     elif(BN1!=BN2):
#         if(count < k):
#             answer += BN1
#             count += 1
#             m-=1
#         else:
#             answer +=BN2
#             count=0
#             m-=1

# print(answer)
        

count = (m//k+1) + (m%k+1)

answer = count * BN1
answer += (m-count) * BN2
print(answer)