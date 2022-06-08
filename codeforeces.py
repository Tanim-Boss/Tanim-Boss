
m, n = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
for i in b:
    l = 0
    high = m-1
    count = 0
    while l <= high:
        mid = (l+high) // 2
        if a[mid] <= i:
            count = mid+1
            l = mid + 1
        else:
            high = mid - 1
    print(count, end=" ")




