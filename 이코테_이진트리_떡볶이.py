n, m = map(int, input().split())    ## [떡의 개수]와 [최소한 M길이의 떡을 가져가기위한 절단기 최대 높이]

numbers=list(map(int, input().split())) ## 떡의 길이

start=0
end=max(numbers)
result=0

def binaray_ddakbyugkki(array, target, start, end):
    global result
    if start > end:
        return None
    while start <= end: ## 이진탐색 시작
        count=0
        mid = (start + end) // 2    ## 중간값 탐색
        
        for i in array: ## 중간값보다 크면 떡이 남으니까 남은 길이들을 다 더해준다 
            if i > mid:
                count += (i-mid)
        
        if count < target: ## 절단하고 남은 떡의 길이가 target보다 작으면 즉, 절단기의 높이가 너무 크다
            end = mid - 1  
        else:              ## 절단하고 남은 떡의 길이가 taget보다 크거나 같은데 즉, 절단기의 높이가 너무 낮으므로 조금씩 높이를 높여서 M으로 맞춘다
            result = mid
            start = mid + 1
    return result


print(binaray_ddakbyugkki(numbers, m, start, end))