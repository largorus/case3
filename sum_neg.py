def sum_neg_between(A):
    if len(A) < 2:
        return 0

    i_max = 0
    i_min = 0

    for i in range(1, len(A)):
        if A[i] > A[i_max]:
            i_max = i
        if A[i] < A[i_min]:
            i_min = i

    left = min(i_max, i_min)
    right = max(i_max, i_min)

    s = 0
    for i in range(left + 1, right):
        if A[i] < 0:
            s += A[i]

    return s
