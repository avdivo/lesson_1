def Merge(A, p, q, r):
    i = p - 1
    j = q
    n = []
    while i < q and j < r:
        if A[i] < A[j]:
            n.append(A[i])
            i += 1
        else:
            n.append(A[j])
            j += 1
    n += A[i:q] + A[j:r]
    A[p - 1:r] = n


def Sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        Sort(A, p, q)
        Sort(A, q + 1, r)
        Merge(A, p, q, r)

A = []
Sort(A, 1, len(A))
assert A == [], 'Ошибка сортировки []'

A = [1]
Sort(A, 1, len(A))
assert A == [1], 'Ошибка сортировки [1]'

A = [2, 1]
Sort(A, 1, len(A))
assert A == [1, 2], 'Ошибка сортировки [2, 1]'

A = [2, 1, 3]
Sort(A, 1, len(A))
assert A == [1, 2, 3], 'Ошибка сортировки [2, 1, 3]'

A = [2, 1, 3, 6, 0, 2]
Sort(A, 1, len(A))
assert A == [0, 1, 2, 2, 3, 6], 'Ошибка сортировки [2, 1, 3, 6, 0, 2]'