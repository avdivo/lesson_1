# n = int(input())
# i = 1
# while i <= n:
#     print('   ' * (n-i), end = '')
#     j, c = i, 1
#     while j <= i:
#         print(j, ' ', end = '')
#         if j == 1:
#             c = -1
#         j -= c
#     print()
#     i += 1


n = int(input())
out = [' '] * (n * 2 - 1)
i = 1
while i <= n:
    out[n-i] = out[~(n-i)] = i
    i += 1
    print(*out) 


# n = int(input())
out = [' '] * (n * 2 - 1)
for i in range(1, n+1):
    out[n-i] = out[~(n-i)] = i
    print(*out) 
