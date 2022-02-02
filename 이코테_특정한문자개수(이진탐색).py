from bisect import bisect_left, bisect_right

n, m = map(int, input().split())

numbers=list(map(int, input().split()))

def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a, left_value)
    return right_index-left_index

if (count_by_range(numbers, m, m)) != 0:
    print(count_by_range(numbers, m, m))
else:
    print(-1)
