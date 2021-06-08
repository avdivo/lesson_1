m, n = 1, 10000000

# sum1 = 0
 
# for i in range(m, n + 1):
#     sum1 += i ** 2 if i % 2 != 0 else 0

# print ('my Медленная')    
# print (sum1)

print ('2 Быстрее')    
print(sum([x**2 for x in range(m, n + 1) if x & 1]))

print ('3 Еще быстрее')    
print(sum(x*x for x in range(m, n + 1) if x%2))

print ('4 Очень быстро')    
print(sum(x*x for x in range((m,m+1)[~m%2], n + 1, 2)))

print ('4 Пуля')    
def sum_odd_quat(x):
    return x * (4*x*x - 1) // 3
    
if abs(m) > abs(n):
    m, n = n, m 
 
sn = sum_odd_quat((abs(n) + 1) // 2)
 
if n*m > 0:
    sm = sum_odd_quat(abs(m)//2)
    print(sn - sm)
else:
    sm = sum_odd_quat((abs(m) + 1)//2)
    print(sn + sm)