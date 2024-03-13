def Merge_Sort(A):
    if len(A) < 2:
        return A
    sorted_list = []
    n = len(A) // 2
    L = Merge_Sort(A[:n])
    R = Merge_Sort(A[n:])
    while (len(L) > 0 and len(R) > 0):
        if L[0] > R[0]:
            sorted_list.append(R[0])
            R.pop(0)
            print(sorted_list)
        else:
            sorted_list.append(L[0])
            L.pop(0)
            print(sorted_list)

    sorted_list += L
    sorted_list += R
    return sorted_list

A = [2, 5, 3, 9, 8, 1, 2, 3]
a = Merge_Sort(A)

print(a)