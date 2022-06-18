



def Merge(A, p, q, r):
    if p == q:
        return
    i = p - 1
    j = q - 1
    n = []
    while i < q and j < r:
        if A[i] < A[j]:
            n.append(A[i])
            i += 1
        else:
            n.append(A[j])
            j += 1
    n += A[i:q] + A[j:r]
    A[p:r] = n


def Sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        Sort(A, p, q)
        Sort(A, q + 1, r)
        Merge(A, p, q, r)

# A = [2, 6, 7, 3, 2, 9, 1, 0, 6, 3]
A = [9, 2]
Sort(A, 1, len(A))
print(A)