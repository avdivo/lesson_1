



def Merge(A, p, q, r):
    p -= 1
    n = []
    for i in range(q-p):
        n.append(min(A[p+i], A[q+i]))
        n.append(max(A[p+i], A[q+i]))
    if r-q > q-p:
        n.append(A[-1])
    A[p:r] = n

def Sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        Sort(A, p, q)
        Sort(A, q + 1, r)
        Merge(A, p, q, r)

# A = [2, 6, 7, 3, 2, 9, 1, 0, 6, 3]
A = [9, 2, 4]
Sort(A, 1, len(A))
print(A)