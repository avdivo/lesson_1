n = int(input())
stadium = list(map(int, input().split()))
_max, ok = divmod(sum(stadium), n)
print(sum(x > _max for x in stadium) if not ok else -1)
