def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = quicksort(a)
b = quicksort(b)

max_profit = 0
for i in range(n):
    max_profit += a[i] * b[i]

print(max_profit)
