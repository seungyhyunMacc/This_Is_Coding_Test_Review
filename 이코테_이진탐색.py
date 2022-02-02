from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a, left_value)
    return right_index-left_index

a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))

# def binary_search(array, target, start, end):
#     count=0
#     if start>end:
#         return None
#     mid=(start + end) // 2

#     if count==target:
#         return end
#     elif 


# n, m = map(int, input().split())

# numbers=list(map(int, input().split()))

# start=0
# end=max(numbers)
