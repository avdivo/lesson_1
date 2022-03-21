n = int(input())
a = list(map(int, input().split()))
print(*[sum(a[0:(i + i % 2) // 2]) for i in range(1, n * 2)])