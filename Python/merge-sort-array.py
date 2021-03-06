import copy as cpy

def sort(L):
    A = cpy.copy(L)  # A = L would be a SERIOUS ERROR
    mergeSort(L, 0, len(L), A)

def mergeSort(L, start, end, A):
    if end - start < 2:
        return
    middle = (start + end) // 2
    mergeSort(L, start,  middle, A)
    mergeSort(L, middle, end   , A)
    merge(L, start, middle, end, A)

def merge(L, start, middle, end, A):
    for i in range(start, end):
        A[i] = L[i]
    idx1 = start
    idx2 = middle
    i    = start
    while idx1 < middle and idx2 < end:
        if A[idx1] <= A[idx2]:
            L[i] = A[idx1]; idx1 += 1
        else:
            L[i] = A[idx2]; idx2 += 1
        i += 1
    while idx1 < middle:
        L[i] = A[idx1]; idx1 += 1; i += 1 
    while idx2 < end:
        L[i] = A[idx2]; idx2 += 1; i += 1
    assert idx1 == middle and idx2 == end

# code for testing
import random as rnd

def demo():
    L = [ rnd.randrange(1, 200) for n in range(1, 16) ]
    print("L = ", L)
    sort(L)
    print("L = ", L)

# n iterations for lists of length k
def testSort(n, k):
    for i in range(1, n+1):
        L = [ rnd.randrange(1, 2*k) for x in range(200) ]
        OldL = L
        sort(L)
        isOrdered(L)
        sameElements(OldL, L)
        print('.', end='')
    print()
    print("All tests successful!")


def isOrdered(L):
    for i in range(len(L) - 1):
        assert L[i] <= L[i+1]

def sameElements(L, S):
    assert set(L) == set(S)

demo()
testSort(100, 200)
