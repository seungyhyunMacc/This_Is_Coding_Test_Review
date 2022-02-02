n = int(input())
Allparts = list(map(int, input().split())) 

m = int(input())
Wantparts = list(map(int, input().split())) 

Allparts.sort()
Wantparts.sort()

start = 0
end = n-1

def binary_search(array, target, start, end):
    if start> end:
        return None
    while start <= end:
        mid = (start + end) // 2

        if array[mid]==target:  ## 리턴1 을 하고 끝
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(Allparts, Wantparts[i], start, end) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
    




