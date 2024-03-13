def Insertion_Sort(A):
    for i in range(len(A)):
        key = A[i]
        print(A)
        for j in range(i, -1, -1):
            if key < A[j]:
                A[j+1] = A[j]
                A[j] = key
            else:
                pass
    return A

A = [2, 5, 3, 9, 8, 1, 2, 3]
a = Insertion_Sort(A)
print(a)